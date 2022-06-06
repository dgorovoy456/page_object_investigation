from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from config.config import TestData


class HomePage(BasePage):

    HEADER = (By.CSS_SELECTOR, 'div[class="header"]')
    LOGO_IMG = (By.CSS_SELECTOR, 'div[class="logo-image"]')
    PRIVATE_CABINET = (By.CSS_SELECTOR, 'div[class="reg-block"]')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    def get_home_page_title(self, title):
        return self.get_title(title)

    def is_header_visible(self):
        return self.is_visible(self.HEADER)

    def get_header_value(self):
        if self.is_visible(self.HEADER):
            return self.get_element_text(self.HEADER)





