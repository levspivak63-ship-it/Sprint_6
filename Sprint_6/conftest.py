import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os


@pytest.fixture(scope="function")
def driver():
    firefox_options = webdriver.FirefoxOptions()
    firefox_options.binary_location = r"C:\Program Files\Mozilla Firefox\firefox.exe"
    
    driver_path = os.path.join(os.getcwd(), "drivers", "geckodriver.exe")
    service = Service(driver_path)
    driver = webdriver.Firefox(service=service, options=firefox_options)
    driver.implicitly_wait(3)
    
    driver.maximize_window()
    
    # Открываем главную страницу
    driver.get("https://qa-scooter.praktikum-services.ru/")
    
    # Закрываем cookie баннер - кликаем на кнопку "да все привыкли"
    try:
        cookie_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'да все привыкли')]"))
        )
        cookie_button.click()
        
        # Ждем исчезновения баннера
        WebDriverWait(driver, 3).until(
            EC.invisibility_of_element_located((By.XPATH, "//button[contains(text(), 'да все привыкли')]"))
        )
        
    except Exception:
        # Баннер не найден или уже закрыт - продолжаем выполнение
        pass
    
    yield driver
    driver.quit()