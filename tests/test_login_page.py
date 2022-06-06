from tests.base_test import BaseTest
from pages.login_page import LoginPage
from config.config import TestData


class TestLogin(BaseTest):

    def test_search_filed_is_visible(self):
        self.login_page = LoginPage(self.driver)
        flag = self.login_page.is_search_exist()
        assert flag

    def test_search_title(self):
        self.login_page = LoginPage(self.driver)
        flag = self.login_page.get_title(TestData.LOGIN_TITLE)
        assert flag == TestData.LOGIN_TITLE

    def test_do_search(self):
        self.login_page = LoginPage(self.driver)
        self.login_page.do_search('some')

