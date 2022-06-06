import pytest
from tests.base_test import BaseTest
from pages.home_page import HomePage
from config.config import TestData


class TestHomePage(BaseTest):

    def test_home_page_title(self):
        self.home_page = HomePage(self.driver)
        flag = self.home_page.get_home_page_title(TestData.LOGIN_TITLE)
        assert flag == TestData.LOGIN_TITLE
