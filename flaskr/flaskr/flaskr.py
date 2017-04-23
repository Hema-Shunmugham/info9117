import os
import sqlite3
import re

from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash

os.environ['FLASK_APP'] = 'flaskr' # to avoid error msg

app = Flask(__name__) # create the application instance :)
app.config.from_object(__name__) # load config from this file , flaskr.py

# Load default config and override config from an environment variable
app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'flaskr.db'),
    SECRET_KEY='development key',
    USERNAME='admin',
    PASSWORD='default'
))


app.config.from_envvar('FLASKR_SETTINGS', silent=True)

def connect_db():
    rv = sqlite3.connect(app.config['DATABASE'])
    rv.row_factory = sqlite3.Row
    return rv

def init_db(schema='schema.sql'):
    db = get_db()
    with app.open_resource(schema, mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()

@app.cli.command('initdb')

def initdb_command():
    init_db()
    print('Initialized the database.')

def get_db():
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db

@app.teardown_appcontext
def close_db(error):
    """Closes the database again at the end of the request."""
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()

@app.route('/')
def show_entries():
    db = get_db()
    cur = db.execute('select username, password from users order by id desc')
    entries = cur.fetchall()
    return render_template('show_entries.html', entries=entries)

def query_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv

@app.route('/add', methods=['POST'])
def add_entry():
    if not session.get('logged_in'):
        abort(401)
    password = request.form['password']
    x = True
    while x:
        if len(password) < 8 :
            break
        elif not re.search("[0-9]", password):
            break
        elif not re.search("[A-Z]", password):
            break
        else:
            print("Valid Password")
            x = False
            break
    if x:
        flash("Not a Valid Password. Password should be minimum 8 letters long with at least one capital letter a number")
    else:
        db = get_db()
        db.execute('insert into users (username, password) values (?, ?)',
                     [request.form['username'], request.form['password']])
        db.commit()
        flash('New entry was successfully posted')
    return redirect(url_for('show_entries'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password =  request.form['password']
        user = query_db('select * from users where username = ?',
                        [username], one=True)
        userPassword = query_db('select * from users where password = ?',
                        [password], one=True)
        if (request.form['username'] != app.config['USERNAME']) and user is None:
            error = 'Invalid username'
        elif (request.form['password'] != app.config['PASSWORD']) and userPassword is None:
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            flash('You were logged in')
            return redirect(url_for('show_entries'))
    return render_template('login.html', error=error)


@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('show_entries'))

@app.route('/shutdown')
def shutdown():
    if app.environment == 'test':
        shutdown_server()
    return "Server shutdown"

@app.cli.command('start')
def start():
    app.config.from_object(__name__) # load config from this file

    app.config.update(dict(
        DATABASE=os.path.join(app.root_path, 'flaskr.db'),
        SECRET_KEY='Production key',
    ))
    app.config.from_envvar('FLASKR_SETTINGS',  silent=True)

    app.run()


def test_server():
    ### Setup for integration testing
    app.config.from_object(__name__) # load config from this file

    app.config.update(dict(
        DATABASE=os.path.join(app.root_path, 'flaskr_test.db'),
        SECRET_KEY='Test key',
        SERVER_NAME='localhost:59407',
        # DEBUG=True, # does not work from behave
    ))
    app.config.from_envvar('FLASKR_TEST_SETTINGS',  silent=True)
    app.environment = 'test'
    with app.app_context():
        init_db('test_schema.sql')
    app.run()


def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError("Not running with Werkzeug server")
    if app.environment == 'test':
        func()
        os.unlink(app.config['DATABASE'])

if __name__ == '__main__':
    start()