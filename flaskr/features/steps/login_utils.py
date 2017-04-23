# coding=utf-8
def login(context, username='admin', password='default'):
    driver = context.browser
    driver.get(context.server_address + "/login")
    uname = driver.find_element_by_name('username')
    passwd = driver.find_element_by_name('password')
    login_button = driver.find_element_by_id('btn_login')
    uname.clear();
    passwd.clear();
    uname.send_keys(username)
    passwd.send_keys(password)
    login_button.click()

def logout(context):
    pass