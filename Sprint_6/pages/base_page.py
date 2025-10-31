# base_page.py

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import Config
from locators import CommonLocators
import allure


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.config = Config

    @allure.step("Найти элемент {locator}")
    def find_element(self, locator, time=3):
        return WebDriverWait(self.driver, time).until(
            EC.presence_of_element_located(locator)
        )

    @allure.step("Кликнуть на элемент {locator}")
    def click_element(self, locator, time=3):
        element = WebDriverWait(self.driver, time).until(
            EC.element_to_be_clickable(locator)
        )
        element.click()

    @allure.step("Дождаться видимости элемента {locator}")
    def wait_for_visibility(self, locator, time=3):
        return WebDriverWait(self.driver, time).until(
            EC.visibility_of_element_located(locator)
        )

    @allure.step("Дождаться кликабельности элемента {locator}")
    def wait_for_clickable(self, locator, time=3):
        return WebDriverWait(self.driver, time).until(
            EC.element_to_be_clickable(locator)
        )

    @allure.step("Скроллить к элементу {locator}")
    def scroll_to_element(self, locator):
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step("Закрыть cookie баннер")
    def close_cookie_banner(self):
        try:
            self.click_element(CommonLocators.COOKIE_BANNER, time=3)
            WebDriverWait(self.driver, 3).until(
                EC.invisibility_of_element_located(CommonLocators.COOKIE_BANNER)
            )
        except:
            pass

    @allure.step("Перейти на сайт")
    def go_to_site(self):
        return self.driver.get(self.config.MAIN_PAGE)

    @allure.step("Дождаться загрузки главной страницы")
    def wait_for_main_page(self, time=3):
        return WebDriverWait(self.driver, time).until(
            EC.url_to_be(self.config.MAIN_PAGE)
        )

    @allure.step("Дождаться загрузки страницы заказа")
    def wait_for_order_page(self, time=3):
        return WebDriverWait(self.driver, time).until(
            EC.url_to_be(self.config.ORDER_PAGE)
        )

    @allure.step("Получить текущий URL")
    def get_current_url(self):
        return self.driver.current_url

    @allure.step("Получить handles окон")
    def get_window_handles(self):
        return self.driver.window_handles

    @allure.step("Получить текущий window handle")
    def get_current_window_handle(self):
        return self.driver.current_window_handle
    
    @allure.step("Ожидать открытия нового окна")
    def wait_for_new_window(self, original_window_count, timeout=5):
        WebDriverWait(self.driver, timeout).until(
            lambda d: len(d.window_handles) > original_window_count
        )
        return True
    
    @allure.step("Ожидать загрузки Дзена")
    def wait_for_dzen(self, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            lambda d: "dzen.ru" in d.current_url
        )
        return True
    
    @allure.step("Переключиться на новое окно")
    def switch_to_new_window(self, original_window):
        for window_handle in self.driver.window_handles:
            if window_handle != original_window:
                self.driver.switch_to.window(window_handle)
                return window_handle