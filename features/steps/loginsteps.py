from behave import given, when, then
from pages.self_healing import self_healing_locator
from pages.locators import *  # Ensure all locators used below are defined


@given('I launch chrome browser')
def step_launch_browser(context):
    # Browser setup typically handled in environment.py
    pass


@when('I open the Touchtight login page')
def step_open_login_page(context):
    element = self_healing_locator(context.page, login_link_xpath, context_name="Login Link")
    element.click()


@when('I enter login email "{email}"')
def step_enter_login_email(context, email):
    element = self_healing_locator(context.page, login_email_input_selectors, context_name="Login Email Input")
    element.fill(email)


@when('I enter login password "{password}"')
def step_enter_login_password(context, password):
    element = self_healing_locator(context.page, password_input_selectors, context_name="Login Password Input")
    element.fill(password)


@when('I click the login button')
def step_click_login_button(context):
    element = self_healing_locator(context.page, button_log_in, context_name="Login Button")
    element.click()


@then('I should be successfully logged into Touchtight')
def step_verify_successful_login(context):
    element = self_healing_locator(context.page, verify_login_success, context_name="Login Success Confirmation")
    assert element.is_visible(), "Login failed: Success element not visible"
