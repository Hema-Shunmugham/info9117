# coding=utf-8

from behave import given, when, then, use_step_matcher
from hamcrest import assert_that, equal_to
import re
from login_utils import *

from behave import *


@given(u'a user visits the site')
def visit(context):
    driver = context.browser
    driver.get(context.home)


@then(u'she should see Coin Mart')
def see(context):
    CoinMart_found = re.search("CoinMart", context.browser.page_source, re.IGNORECASE)
    assert CoinMart_found


@when(u'she logs in')
def logs_in(context):
    login(context)

@when(u'she returns to the site')
def return_visit(context):
    driver = context.browser
    driver.get(context.home)


@then(u'she should see the Logout link')
def step_impl(context):
    logout_found = re.search("log out", context.browser.page_source, re.IGNORECASE)
    assert logout_found