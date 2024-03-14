class Page:
    def __init__(self, driver):
        self.driver = driver

    def open(self, url):
        self.driver.get(url)

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def click(self, *locator):
        self.driver.find_element(*locator).click()

    def input_text(self, text, *locator):
        self.driver.find_element(*locator).send_keys(text)

    def find_elements(self, *locator):
        return self.driver.find_elements(*locator)

    def verify_partial_text(self, expected_text, *locator):
        actual_text = self.driver.find_element(*locator).text
        assert expected_text in actual_text, f'Expected {expected_text} not in {actual_text}'

    def verify_partial_url(self, expected_partial_url):
        actual_url = self.driver.current_url
        assert expected_partial_url in actual_url, f'Expected {expected_partial_url} not in {actual_url}'

    def verify_url(self, expected_url):
        actual_url = self.driver.current_url
        assert expected_url == actual_url, f'Expected {expected_url} but got {actual_url}'

    def verify_text(self, expected_text, *locator):
        actual_text = self.driver.find_element(*locator).text
        assert expected_text == actual_text, f'Expected {expected_text} but not {actual_text}'