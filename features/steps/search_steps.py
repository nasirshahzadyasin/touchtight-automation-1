# from behave import *
# from playwright.sync_api import expect
#
#
# @given('I am on the DuckDuckGo homepage')
# def step_impl(context):
#     context.page.goto("https://duckduckgo.com")
#
#
# @when('I search for "{query}"')
# def step_impl(context, query):
#     context.page.fill('input[name="q"]', query)
#     context.page.keyboard.press("Enter")
#
#
# @then('I should see results containing "{text}"')
# def step_impl(context, text):
#     results_locator = context.page.locator(f"text={text}").first
#     expect(results_locator).to_be_visible()
