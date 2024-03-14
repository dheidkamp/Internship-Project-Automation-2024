from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

EMAIL_FIELD = (By.CSS_SELECTOR, "input[id='email-2']")
PW_FIELD = (By.CSS_SELECTOR, "input[id='field']")
Continue_BTN = (By.CSS_SELECTOR, "a[wized='loginButton']")


@given('Open the signin page')
def open_main_page(context):
    # context.driver.get('https://soft.reelly.io/sign-in')
    context.app.login_page.open_main_page()

@when('Log in to the page')
def input_search(context):
    # context.driver.find_element(*EMAIL_FIELD).send_keys('dheidkamp.heidkamp3@gmail.com')
    # context.driver.find_element(*PW_FIELD).send_keys('Amerikamp2021')
    # context.driver.find_element(*Continue_BTN).click()
    # sleep(4)
    context.app.login_page.input_search()