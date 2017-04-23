# coding=utf-8
import os
import tempfile
import pytest
from flaskr import flaskr


@pytest.fixture
def client(request):
    db_fd, flaskr.app.config['DATABASE'] = tempfile.mkstemp()
    flaskr.app.config['TESTING'] = True
    client = flaskr.app.test_client()
    with flaskr.app.app_context():
        flaskr.init_db()
    def teardown():
        os.close(db_fd)
        os.unlink(flaskr.app.config['DATABASE'])
    request.addfinalizer(teardown)
    return client


def login(client, username, password):
    return client.post('/login', data=dict(
        username=username,
        password=password
    ), follow_redirects=True)


def logout(client):
    return client.get('/logout', follow_redirects=True)


def test_empty_db(client):
    rv = client.get('/')
    assert b'Unbelievable.  No entries here so far' in rv.data


def test_login_logout(client):
    rv = login(client, flaskr.app.config['USERNAME'],
               flaskr.app.config['PASSWORD'])
    assert b'You were logged in' in rv.data
    rv = logout(client)
    assert b'You were logged out' in rv.data
    rv = login(client, flaskr.app.config['USERNAME'] + 'x',
               flaskr.app.config['PASSWORD'])
    assert b'Invalid username' in rv.data
    rv = login(client, flaskr.app.config['USERNAME'],
               flaskr.app.config['PASSWORD'] + 'x')
    assert b'Invalid password' in rv.data

def test_login_incorrect_credentials(client):
    with client as c:
        rv = c.post('/login', data=dict(
            username=flaskr.app.config['USERNAME'] + 'x',
            password=flaskr.app.config['PASSWORD']
        ), follow_redirects=True)
        assert b'Invalid username' in rv.data

        rv = c.post('/login', data=dict(
            username=flaskr.app.config['USERNAME'],
            password=flaskr.app.config['PASSWORD'] + 'x'
        ), follow_redirects=True)
        assert b'Invalid password' in rv.data

def test_add_entries_login(client):
    with client as c:
        rv = login(client, flaskr.app.config['USERNAME'],
                   flaskr.app.config['PASSWORD'])
        assert b'You were logged in' in rv.data
        rv = client.post('/add', data=dict(
            username='test',
            password='Hema7067'
        ), follow_redirects=True)
        assert b'New entry was successfully posted' in rv.data

def test_add_entries_logout(client):
    with client as c:
        rv = c.post('/add', data=dict(
            username=flaskr.app.config['USERNAME'],
            password=flaskr.app.config['PASSWORD']
        ), follow_redirects=True)
        assert b'You were logged out' not in rv.data

def test_messages(client):
    rv = login(client, flaskr.app.config['USERNAME'],
               flaskr.app.config['PASSWORD'])
    assert b'You were logged in' in rv.data
    rv = client.post('/add', data=dict(
        username='test',
        password='test'
    ), follow_redirects=True)
    assert b'Not a Valid Password. Password should be minimum 8 letters long with at least one capital letter a number' in rv.data
