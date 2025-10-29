import pytest
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from pages.main_page import MainPage
from pages.order_page import OrderPage


class TestLogos:
    
    @allure.title("Проверка перехода на главную страницу при клике на логотип Самоката")
    def test_click_scooter_logo_returns_to_main_page(self, driver):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)

        main_page.go_to_site()

        main_page.click_order_button_top()

        order_page.wait_for_load_order_page()

        with allure.step("Клик на логотип Самоката со страницы заказа"):
            main_page.click_scooter_logo()

        with allure.step("Проверка возврата на главную страницу"):
            main_page.wait_for_url(main_page.base_url)
            
            main_page.wait_for_visibility(main_page.ORDER_BUTTON_TOP)

    @allure.title("Проверка открытия Дзена при клике на логотип Яндекса")
    def test_click_yandex_logo_opens_dzen(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_site()
    
        original_window = driver.current_window_handle
    
        with allure.step("Клик на логотип Яндекса"):
            main_page.click_yandex_logo()
    
        with allure.step("Ожидание открытия нового окна"):
            WebDriverWait(driver, 5).until(
                lambda d: len(d.window_handles) == 2
        )
    
        with allure.step("Переключение на новое окно"):
            for window_handle in driver.window_handles:
                if window_handle != original_window:
                    driver.switch_to.window(window_handle)
                    break
                    
        with allure.step("Ожидание загрузки Дзена"):
            WebDriverWait(driver, 10).until(
                lambda d: "dzen.ru" in d.current_url
        )

        with allure.step("Проверка загрузки Дзена"):
            current_url = driver.current_url
            assert "dzen.ru" in current_url, f"Текущий URL: {current_url}, ожидался Дзен"