from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@when('Click on “off plan” at the left side menu')
def click_off_plan(context):
    # context.driver.find_element(*OFF_PLAN).click()
    context.app.main_page.click_off_plan()
