from selenium.webdriver.common.by import By
from time import sleep
from pages.base_page import Page


class OffPlan(Page):
    FILTERS_BTN = (By.CSS_SELECTOR, "a[wized='openFiltersWindow'] [class='filter-text']")
    LAST_UNITS = (By.CSS_SELECTOR, "div[wized='priorityStatusLastUnits'] [class='tag-text-proparties']")
    APPLY_FILTER = (By.CSS_SELECTOR, "a[wized='applyFilterButton']")
    ALL_LISTINGS = (By.CSS_SELECTOR, "[wized='cardOfProperty']")
    LAST_UNITS_TAG = (By.CSS_SELECTOR, "div[class='commision_box']")

    def verify_right_page(self, expected_part_url):
        self.verify_partial_url(expected_part_url)

    def filter_by_sale_status(self):
        self.find_element(*self.FILTERS_BTN).click()
        self.find_element(*self.LAST_UNITS).click()


    def verify_last_units(self):
        all_listings = self.find_elements(*self.ALL_LISTINGS)
        for listing in all_listings:
            last_units_tag = listing.find_elements(*self.LAST_UNITS_TAG)
            assert len(last_units_tag) > 0, f'Listing does not have "Last Units" tag'
