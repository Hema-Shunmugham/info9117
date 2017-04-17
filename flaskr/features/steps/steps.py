@given(u'a user visits the site')
def impl(context):
    context.browser.visit('/')

@then(u'I should see the message {auth_message}')
def imple(context):
    assert False

@when(u'I log in as "registeredUser"')
def step_impl(context):
    username_field = context.browser.find_by_id('username')
    password_field = context.browser.find_by_id('password')
    username_field.send_keys('registeredUser')
    password_field.send_keys('1234')
    submit_button = context.browser.find_by_id('submit')
    submit_button.click()

@when(u'I log in as "unregisteredUser"')
def step_impl(context):
    username_field = context.browser.find_by_id('username')
    password_field = context.browser.find_by_id('password')
    username_field.send_keys('unregisteredUser')
    password_field.send_keys('1234')
    submit_button = context.browser.find_by_id('submit')
    submit_button.click()