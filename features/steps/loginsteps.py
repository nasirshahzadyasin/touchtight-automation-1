from behave import *
from pages.self_healing import self_healing_locator
from pages.locators import *


@given('I launch chrome browser')
def browser(context):
    pass


@when('I open touchtight login page')
def goto_login(context):
    element = self_healing_locator(context.page, login_link_xpath, context_name="Login")
    element.click()


@when('Enter login email "{login_email}"')
def enter_email(context, login_email):
    element = self_healing_locator(context.page, login_email_input_selectors, context_name="Email Input")
    element.fill(login_email)


@when('Enter login password "{login_pwd}"')
def pwd_input(context, login_pwd):
    element = self_healing_locator(context.page, password_input_selectors, context_name="Password Input")
    element.fill(login_pwd)


@when('Click the login button')
def click_login(context):
    element = self_healing_locator(context.page, button_log_in, context_name="Log In")
    element.click()


@then('User must successfully login to the touchtight')
def Verify(context):
    element = self_healing_locator(context.page, verify_login_success, context_name="My Library")
    element.click()


@given('I am on home page')
def home(context):
    pass


@when('click the profile icon')
def profile_icon(context):
    element = self_healing_locator(context.page, profile_icon_xpath, context_name="Profile icon")
    element.click()


@when('Click logout button')
def logout_button(context):
    element = self_healing_locator(context.page, logout_btn_xpath, context_name="Log out")
    element.click()


@then('Verify that logged out successfully')
def verify_after(context):
    element = self_healing_locator(context.page, home_text_path, context_name="Homepage_logged out")
    element.click()
