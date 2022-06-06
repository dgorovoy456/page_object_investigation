import pytest
from selenium import webdriver
from config.config import TestData


@pytest.fixture(params=["chrome", "firefox"], scope='class', autouse=True)
def init_driver(request):
    if request.param == "chrome":
        driver = webdriver.Chrome(executable_path=TestData.CHROME_DRIVER)
    elif request.param == "firefox":
        driver = webdriver.Firefox(executable_path=TestData.FIREFOX_DRIVER)

    request.cls.driver = driver

    yield

    driver.close()
