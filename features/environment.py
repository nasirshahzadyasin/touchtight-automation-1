from playwright.sync_api import sync_playwright
import subprocess
import os


def before_all(context):
    # Get command-line parameters
    userdata = context.config.userdata
    context.base_url = userdata.get('base_url', 'https://fe.stag.touchtight.com/')
    browser_type = userdata.get('browser', 'chromium')
    headless = userdata.get('headless', 'false').lower() == 'true'

    # Initialize Playwright
    context.playwright = sync_playwright().start()

    # Browser launch
    context.browser = getattr(context.playwright, browser_type).launch(
        headless=headless,
        args=['--start-maximized']
    )


def after_all(context):
    context.browser.close()
    context.playwright.stop()


def before_scenario(context, scenario):
    context.page = context.browser.new_page()
    # context.page.set_viewport_size({"width": 1920, "height": 1180})
    # Navigate to base URL at scenario start
    context.page.goto(context.base_url)


def after_scenario(context, scenario):
    context.page.close()
