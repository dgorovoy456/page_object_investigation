from config.config import TestData
from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    """By locators - OR"""
    SEARCH = (By.ID, 'search')

    """constructor of the page class"""
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    """Page Actions"""

    """this is used to get page title"""
    def get_login_page_title(self, title):
        return self.get_title(title)

    """this is used to check search link"""
    def is_search_exist(self):
        return self.is_visible(self.SEARCH)

    """this is used to search by key word"""
    def do_search(self, key_word: str):
        self.do_send_keys(self.SEARCH, key_word)
        self.press_enter(self.SEARCH)