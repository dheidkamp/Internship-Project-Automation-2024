from selenium.webdriver.common.by import By

from pages.base_page import Page


class MainPage(Page):
    OFF_PLAN = (By.CSS_SELECTOR, "a[href='/off-plan'] [class='menu-button-text']")

    def click_off_plan(self):
        self.click(*self.OFF_PLAN)
