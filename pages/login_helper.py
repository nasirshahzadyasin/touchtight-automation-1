from pages.self_healing import self_healing_locator
from pages.locators import *


def login_user(context, email, password):
    page = context.page
    page.goto(f"{context.base_url}login")

    email_input = self_healing_locator(page, login_email_input_selectors, context_name="Email Input")
    email_input.fill(email)  # Make sure `email` is passed in

    password_input = self_healing_locator(page, password_input_selectors, context_name="Password Input")
    password_input.fill(password)  # Same here

    login_btn = self_healing_locator(page, button_log_in, context_name="Login Button")
    login_btn.click()
