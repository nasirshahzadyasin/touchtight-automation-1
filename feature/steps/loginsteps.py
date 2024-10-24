import time

from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By


@given('I launch chrome browser')
def Launch_browser(context):
    options = webdriver.ChromeOptions()
    context.driver = webdriver.Chrome(options=options)


@when('I open touchtight login page')
def Open_app(context):
    context.driver.get("https://fe.stag.touchtight.com/login")


@when('Enter username "{user}" and password "{pwd}"')
def Enter_login_details(context, user, pwd):
    try:
        context.driver.find_element(By.ID, "mui-1").send_keys(user)
        context.driver.find_element(By.ID, "mui-2").send_keys(pwd)
    except:
        assert False, "Test Failed"


@when('Click the login button')
def Click_login_button(context):
    try:
        context.driver.find_element(By.ID, "mui-3").click()
        time.sleep(5)
    except:
        assert False, "Test Failed"


@then('User must successfully login to the touchtight')
def Verif_login(context):
    try:
        context.driver.find_element(By.ID, "mui-5").click()
        time.sleep(5)
        context.driver.close()
    except:
        context.driver.close()
        assert False, "Test Failed"
