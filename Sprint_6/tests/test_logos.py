# test_logos.py

import pytest
import allure
from pages.main_page import MainPage
from pages.order_page import OrderPage
from helpers import WindowHelper


class TestLogos:
    
    @allure.title("Проверка перехода на главную страницу при клике на логотип Самоката")
    def test_click_scooter_logo_returns_to_main_page(self, driver):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)

        main_page.go_to_site()
        main_page.close_cookie_banner()
        main_page.click_order_button_top()
        order_page.wait_for_load_order_page()

        with allure.step("Кликнуть на логотип Самоката"):
            main_page.click_scooter_logo()

        with allure.step("Проверить возврат на главную страницу"):
            main_page.wait_for_main_page()
            assert main_page.is_order_button_top_visible()

    @allure.title("Проверка открытия Дзена при клике на логотип Яндекса")
    def test_click_yandex_logo_opens_dzen(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_site()
        main_page.close_cookie_banner()
    
        original_window = main_page.get_current_window_handle()
        original_count = len(main_page.get_window_handles())
    
        with allure.step("Кликнуть на логотип Яндекса"):
            main_page.click_yandex_logo()
    
        with allure.step("Ожидать открытия нового окна"):
            WindowHelper.wait_for_new_window(driver, original_count)
    
        with allure.step("Переключиться на новое окно"):
            WindowHelper.switch_to_new_window(driver, original_window)
                    
        with allure.step("Ожидать загрузки Дзена"):
            WindowHelper.wait_for_dzen(driver)
    
        with allure.step("Проверить загрузку Дзена"):
            current_url = main_page.get_current_url()
            assert "dzen.ru" in current_url