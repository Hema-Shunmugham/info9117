from behave import *

@given(u'CoinMart is set up')
def flask_is_set_up(context):
    assert context.client

@given(u'I am not logged in')
def logout(context):
    context.page = context.client.get('/logout', follow_redirects=True)

@given(u'I log in with "{username}" and "{password}" and redirected to the registration page')
@given(u'I log in with "{username}" and "{password}"')
@when(u'I log in with "{username}" and "{password}"')
def login(context, username, password):
    context.page = context.client.post(
        '/login',
        data=dict(username=username, password=password),
        follow_redirects=True
    )
    assert context.page

@when(u'I log out')
def logout(context):
    context.page = context.client.get('/logout', follow_redirects=True)
    assert context.page


@then(u'I should see the response message "{message}"')
def message(context, message):
    assert str.encode(message) in context.page.data

@when(u'I add a new entry with "{username}" and "{password}" as the username and password')
def add(context, username, password):
    context.page = context.client.post(
        '/add',
        data=dict(username=username, password=password),
        follow_redirects=True
    )
    assert context.page