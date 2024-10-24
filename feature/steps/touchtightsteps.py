from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By


@given('Launch chrome browser')
def LaunchBrowser(context):
    options = webdriver.ChromeOptions()
    context.driver = webdriver.Chrome(options=options)


@when('Open touchtight login page')
def Open_login_page(context):
    context.driver.get("https://fe.stag.touchtight.com/login")


@then('Verify that the logo presence on the page')
def Verify_logo(context):
    status = context.driver.find_element(By.XPATH, "//div/div/img[@alt='logo']").is_displayed()
    assert status is True


@then('close the browser')
def close_browser(context):
    context.driver.close()
