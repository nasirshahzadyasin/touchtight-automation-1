from behave import given, when, then
from pages.self_healing import self_healing_locator
from pages.locators import *  # Ensure all locators used below are defined


@given('I am on the home page')
def step_on_home_page(context):
    # This assumes user is already logged in from previous scenario
    pass


@when('I click the profile icon')
def step_click_profile_icon(context):
    element = self_healing_locator(context.page, profile_icon_xpath, context_name="Profile Icon")
    element.click()


@when('I click the logout button')
def step_click_logout_button(context):
    element = self_healing_locator(context.page, logout_btn_xpath, context_name="Logout Button")
    element.click()


@then('I should see confirmation of successful logout')
def step_verify_logout(context):
    element = self_healing_locator(context.page, home_text_path, context_name="Logged Out Confirmation")
    text = element.inner_text()
    expected_text = "Most Popular"  # Replace with actual logout confirmation message
    assert expected_text in text, f"Logout failed: expected '{expected_text}', got '{text}'"
