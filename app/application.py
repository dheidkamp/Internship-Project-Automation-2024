from pages.base_page import Page
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.off_plan_page import OffPlan

class Application:

    def __init__(self, driver):
        self.page = Page(driver)
        self.login_page = LoginPage(driver)
        self.main_page = MainPage(driver)
        self.off_plan_page = OffPlan(driver)