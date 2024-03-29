from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

FILTERS_BTN = (By.CSS_SELECTOR, "a[wized='openFiltersWindow'] [class='filter-text']")
LAST_UNITS = (By.CSS_SELECTOR, "div[wized='priorityStatusLastUnits'] [class='tag-text-proparties']")
APPLY_FILTER = (By.CSS_SELECTOR, "a[wized='applyFilterButton']")
ALL_LISTINGS = (By.CSS_SELECTOR, "[wized='cardOfProperty']")
LAST_UNITS_TAG = (By.CSS_SELECTOR, "div[class='commision_box']")


@then('Verify {expected_part_url} in url')
def verify_right_page(context, expected_part_url):
    # url = context.driver.current_url
    # assert expected_part_url in url, f'Expected {expected_part_url} but got {url}'
    context.app.off_plan_page.verify_right_page(expected_part_url)


@when('Filter by sale status of “Last Units”')
def filter_by_sale_status(context):
    # context.driver.find_element(*FILTERS_BTN).click()
    # context.driver.find_element(*LAST_UNITS).click()
    # # context.driver.find_element(*APPLY_FILTER).click()
    context.app.off_plan_page.filter_by_sale_status()


@then('Verify each product contains the "Last Units" tag')
def verify_last_units(context):
    # all_listings = context.driver.find_elements(*ALL_LISTINGS)
    # for listing in all_listings:
    #     last_units_tag = listing.find_elements(*LAST_UNITS_TAG)
    #     assert len(last_units_tag) > 0, f'Listing does not have "Last Units" tag'
    context.app.off_plan_page.verify_last_units()
    sleep(2)