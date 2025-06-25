import time

from behave import *
from playwright.sync_api import expect

pricing_xpath = "//a[.//p[contains(text(), 'Pricing')]]"
pricing_title_xpath = "//p[contains(text(), 'Test')]"


@given('I am on the homepage')
def step_impl(context):
    # Already handled in environment.py's before_scenario
    pass  # Keep empty since navigation happens automatically


@when('I click Pricing link button')
def step_impl(context):
    element = context.page.locator(f"xpath={pricing_xpath}")
    time.sleep(5)
    expect(element).to_be_visible()
    element.click()


@then('I should navigate to billing page and verified {text}')
def step_impl(context, text):
    results_locator = context.page.locator(f"text={text}").first
    time.sleep(20)
    expect(results_locator).to_be_visible()
