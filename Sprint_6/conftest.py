# conftest.py

import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from config import Config


@pytest.fixture(scope="function")
def driver():
    service = Service()
    driver = webdriver.Firefox(service=service)
    driver.implicitly_wait(3)
    
    driver.maximize_window()
    driver.get(Config.MAIN_PAGE)
    
    yield driver
    driver.quit()