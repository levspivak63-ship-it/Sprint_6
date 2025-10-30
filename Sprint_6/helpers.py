# helpers.py

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure

class WindowHelper:
    
    @staticmethod
    @allure.step("Ожидать открытия нового окна")
    def wait_for_new_window(driver, original_window_count, timeout=5):
        WebDriverWait(driver, timeout).until(
            lambda d: len(d.window_handles) > original_window_count
        )
        return True
    
    @staticmethod
    @allure.step("Ожидать загрузки Дзена")
    def wait_for_dzen(driver, timeout=10):
        WebDriverWait(driver, timeout).until(
            lambda d: "dzen.ru" in d.current_url
        )
        return True
    
    @staticmethod
    @allure.step("Переключиться на новое окно")
    def switch_to_new_window(driver, original_window):
        for window_handle in driver.window_handles:
            if window_handle != original_window:
                driver.switch_to.window(window_handle)
                return window_handle