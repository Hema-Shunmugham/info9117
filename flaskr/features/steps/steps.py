
from behave import *
import time

@given(u'CoinMart is set up')
def CoinMart_is_set_up(context):
    assert context.home

@given(u'I am not logged in')
def logout(context):
    driver = context.browser
    driver.get('/logout')
    time.sleep(2)

@given(u'I log in with "{username}" and "{password}" and redirected to the registration page')
@given(u'I log in with "{username}" and "{password}"')
@when(u'I log in with "{username}" and "{password}"')
def login(context, username, password):
    driver = context.browser
    driver.get(context.home + "/login")
    uname = driver.find_element_by_name('username')
    passwd = driver.find_element_by_name('password')
    login_button = driver.find_element_by_id('btn_login')
    uname.clear();
    passwd.clear();
    uname.send_keys(username)
    passwd.send_keys(password)
    login_button.click()
    time.sleep(2)

@when(u'I log out')
def logout(context):
    driver = context.browser
    driver.get(context.home + '/logout')
    time.sleep(2)


@then(u'I should see the response message "{message}"')
def message(context, message):
    driver = context.browser
    driver.get(context.home)
    assert str.encode(message)

@when(u'I add a new entry with "{username}" and "{password}" as the username and password')
def add(context, username, password):
    driver = context.browser
    driver.get(context.home + '/')
    uname = driver.find_element_by_name('username')
    passwd = driver.find_element_by_name('password')
    add_button = driver.find_element_by_id('btn_add')
    uname.clear();
    passwd.clear();
    uname.send_keys(username)
    passwd.send_keys(password)
    add_button.click()
    time.sleep(2)