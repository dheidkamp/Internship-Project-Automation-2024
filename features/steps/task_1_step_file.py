from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

EMAIL_FIELD = (By.CSS_SELECTOR, "input[id='email-2']")
PW_FIELD = (By.CSS_SELECTOR, "input[id='field']")
Continue_BTN = (By.CSS_SELECTOR, "a[wized='loginButton']")
OFF_PLAN = (By.CSS_SELECTOR, "a[href='/off-plan'] [class='menu-button-text']")
FILTERS_BTN = (By.CSS_SELECTOR, "a[wized='openFiltersWindow'] [class='filter-text']")
LAST_UNITS = (By.CSS_SELECTOR, "div[wized='priorityStatusLastUnits'] [class='tag-text-proparties']")
APPLY_FILTER = (By.CSS_SELECTOR, "a[wized='applyFilterButton']")
ALL_LISTINGS = (By.CSS_SELECTOR, "[wized='cardOfProperty']")
LAST_UNITS_TAG = (By.CSS_SELECTOR, "div[class='commision_box']")


@given('Open the main page')
def open_main_page(context):
    context.driver.get('https://soft.reelly.io/sign-in')


@when('Log in to the page')
def input_search(context):
    context.driver.find_element(*EMAIL_FIELD).send_keys('dheidkamp.heidkamp3@gmail.com')
    context.driver.find_element(*PW_FIELD).send_keys('Amerikamp2021')
    context.driver.find_element(*Continue_BTN).click()
    sleep(4)


@when('Click on “off plan” at the left side menu')
def click_off_plan(context):
    context.driver.find_element(*OFF_PLAN).click()


@then('Verify {expected_part_url} in url')
def verify_right_page(context, expected_part_url):
    url = context.driver.current_url
    assert expected_part_url in url, f'Expected {expected_part_url} but got {url}'


@when('Filter by sale status of “Last Units”')
def filter_by_sale_status(context):
    context.driver.find_element(*FILTERS_BTN).click()
    context.driver.find_element(*LAST_UNITS).click()
    # context.driver.find_element(*APPLY_FILTER).click()


@then('Verify each product contains the "Last Units" tag')
def verify_last_units(context):
    all_listings= context.driver.find_elements(*ALL_LISTINGS)
    for listing in all_listings:
        last_units_tag = listing.find_elements(*LAST_UNITS_TAG)
        assert len(last_units_tag) > 0, f'Listing does not have "Last Units" tag'


