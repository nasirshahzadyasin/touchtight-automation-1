import os
import time
from behave import *
from pages.self_healing import self_healing_locator
from pages.locators import *


@given('I open touchtight app')
def launch_browser(context):
    pass


@when('I open touchtight signup page')
def goto_signup_page(context):
    element = self_healing_locator(context.page, getStarted_selectors, context_name="Get Started")
    element.click()


@when('Enter email "{email}"')
def email_input(context, email):
    element = self_healing_locator(context.page, email_input_selectors, context_name="Email Input")
    element.fill(email)


@when('Click get started button')
def get_started_btn(context):
    element = self_healing_locator(context.page, getStarted_btn_selectors, context_name="Get Started Button")
    element.click()


@when('Enter fullname "{fullname}"')
def fullname_input(context, fullname):
    element = self_healing_locator(context.page, fullname_input_selectors, context_name="Full Name Input")
    element.fill(fullname)


@when('Enter password "{pwd}"')
def pwd_input(context, pwd):
    element = self_healing_locator(context.page, pwd_input_selectors, context_name="Password Input")
    element.fill(pwd)


@when('Enter application secret key')
def key_input(context):
    key = os.getenv("APP_SECRET_KEY")
    assert key, "APP_SECRET_KEY is not set in environment variables"
    element = self_healing_locator(context.page, appsecret_input_selectors, context_name="App Secret Input")
    element.fill(key)


@when('Enter club name "{club}"')
def club_input(context, club):
    element = self_healing_locator(context.page, club_input_selectors, context_name="Club Name Input")
    element.fill(club)


@when('Click Create Account button')
def create_acc_button(context):
    element = self_healing_locator(context.page, create_acc_btn_selectors, context_name="Create Account Button")
    element.click()


@then('Verify that user account created successfully')
def verify_acc_creation(context):
    element = self_healing_locator(context.page, verify_login_success, context_name="My Library")
    element.click()
