from selenium.webdriver.common.by import By
from time import sleep
from pages.base_page import Page


class LoginPage(Page):
    EMAIL_FIELD = (By.CSS_SELECTOR, "input[id='email-2']")
    PW_FIELD = (By.CSS_SELECTOR, "input[id='field']")
    CONTINUE_BTN = (By.CSS_SELECTOR, "a[wized='loginButton']")

    def open_main_page(self):
        self.open('https://soft.reelly.io/sign-in')

    def input_search(self):
        self.input_text('dheidkamp.heidkamp3@gmail.com', *self.EMAIL_FIELD,)
        self.input_text('Amerikamp2021',*self.PW_FIELD)
        self.click(*self.CONTINUE_BTN)
        sleep(4)