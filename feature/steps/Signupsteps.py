import time

from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By


@given('I open chrome browser')
def Launch_browser(context):
    options = webdriver.ChromeOptions()
    context.driver = webdriver.Chrome(options=options)


@when('I open touchtight signup page')
def Open_app(context):
    context.driver.get("https://fe.stag.touchtight.com/register")
    time.sleep(10)


@when('Enter firstname "{f_name}" and lastname "{l_name}"')
def name_input(context, f_name, l_name):
    context.driver.find_element(By.XPATH, "/html/body/div[5]/div/div[1]/div/div[2]/div[4]/div[1]/div/div/input").send_keys(f_name)
    context.driver.find_element(By.XPATH, "/html/body/div[5]/div/div[1]/div/div[2]/div[4]/div[2]/div/div/input").send_keys(l_name)
    time.sleep(10)


@when('Enter email "{email}"')
def email_input(context, email):
    context.driver.find_element(By.ID, "mui-19").send_keys(email)
    time.sleep(10)


@when('Enter password "{pwd}" and confirm password "{confirm_pwd}"')
def password_input(context, pwd, confirm_pwd):
    context.driver.find_element(By.ID, "mui-20").send_keys(pwd)
    context.driver.find_element(By.ID, "mui-21").send_keys(confirm_pwd)


@when('Enter application secret key "{secret_key}"')
def app_secret_key(context, secret_key):
    context.driver.find_element(By.ID, "mui-22").send_keys(secret_key)


@when('Click Check box')
def check_box(context):
    context.driver.find_element(By.XPATH, "//div//fieldset//label//span//input[@type='checkbox']").click()


@when('Click Create Account button')
def create_account_btn(context):
    context.driver.find_element(By.ID, "mui-23").click()


@then('Verify "Thanks for registering!! Please confirm your email. We have sent a link", link sent successfully')
def signup_success_verify(context):
    context.driver.find_element(By.ID, "notistack-snackbar").click()
