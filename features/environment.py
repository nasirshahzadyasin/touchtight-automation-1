from playwright.sync_api import sync_playwright
from pages.login_helper import login_user


def before_all(context):
    from playwright.sync_api import sync_playwright
    context.base_url = context.config.userdata.get('base_url', 'https://fe.stag.touchtight.com/')
    context.browser_type = context.config.userdata.get('browser', 'chromium')
    context.headless = context.config.userdata.get('headless', 'true').lower() == 'true'
    context.email = context.config.userdata.get("email", "testns0222+0290@gmail.com")
    context.password = context.config.userdata.get("password", "P@ss1234")
    context.is_logged_in = False
    context.page = None
    context.browser = None
    context.playwright = sync_playwright().start()


def before_scenario(context, scenario):
    if context.browser is None:
        context.browser = getattr(context.playwright, context.browser_type).launch(
            headless=context.headless,
            args=['--start-maximized']
        )

    if context.page is None or context.page.is_closed():
        context.page = context.browser.new_page()
        context.page.goto(context.base_url)  # Open the home/login page

    if 'login_required' in scenario.tags and not context.is_logged_in:
        from pages.login_helper import login_user
        login_user(context, context.email, context.password)
        context.is_logged_in = True


def after_all(context):
    if context.page:
        context.page.close()
    if context.browser:
        context.browser.close()
    if context.playwright:
        context.playwright.stop()
