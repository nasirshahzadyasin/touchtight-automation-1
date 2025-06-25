from playwright.sync_api import sync_playwright
import subprocess
import os

from pages.login_helper import login_user


def before_all(context):
    # Get command-line parameters
    userdata = context.config.userdata
    context.base_url = userdata.get('base_url', 'https://fe.stag.touchtight.com/')
    browser_type = userdata.get('browser', 'chromium')
    headless = userdata.get('headless', 'true').lower() == 'true'  # default to headless=True

    # Initialize Playwright
    context.playwright = sync_playwright().start()

    # Launch the browser
    context.browser = getattr(context.playwright, browser_type).launch(
        headless=headless,
        args=['--start-maximized']
    )

    # Create a new page
    context.page = context.browser.new_page()

    # ✅ Initialize flag here
    context.is_logged_in = False


def after_all(context):
    if hasattr(context, "browser"):
        context.browser.close()
    if hasattr(context, "playwright"):
        context.playwright.stop()


def before_scenario(context, scenario):
    if 'login_required' in scenario.tags:
        if not hasattr(context, "is_logged_in") or not context.is_logged_in:
            email = context.config.userdata.get("email", "testns0222+0290@gmail.com")
            password = context.config.userdata.get("password", "P@ss1234")
            assert email and password, "Missing email or password from CLI or config"
            login_user(context, email, password)
            context.is_logged_in = True


def after_scenario(context, scenario):
    context.page.close()
