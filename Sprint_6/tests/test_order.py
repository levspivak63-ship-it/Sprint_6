# test_order.py

import pytest
import allure
from pages.order_page import OrderPage
from data import TestData


class TestOrder: 

    @allure.title("Проверка заказа самоката через верхнюю кнопку")
    def test_successful_order_flow_top_button(self, driver): 
        order_page = OrderPage(driver)
        order_page.go_to_site()
        order_page.close_cookie_banner()

        with allure.step("Начать заказ через верхнюю кнопку"):
            order_page.click_top_order_button()

        with allure.step("Заполнить первую страницу заказа"):
            order_page.fill_first_step_form(
                name=TestData.ORDER_DATA_1["name"],
                last_name=TestData.ORDER_DATA_1["last_name"],
                address=TestData.ORDER_DATA_1["address"],
                phone=TestData.ORDER_DATA_1["phone"],
                metro_station=TestData.ORDER_DATA_1["metro_station"]
            )

        with allure.step("Заполнить вторую страницу заказа"):
            order_page.fill_second_step_form(
                delivery_day=TestData.ORDER_DATA_1["delivery_day"],
                period=TestData.ORDER_DATA_1["period"],
                color=TestData.ORDER_DATA_1["color"],
                comment=TestData.ORDER_DATA_1["comment"]
            )

        with allure.step("Подтвердить заказ"):
            order_page.confirm_order()

        with allure.step("Проверить успешное оформление заказа"):
            success_message = order_page.get_success_message()
            assert "Заказ оформлен" in success_message

    @allure.title("Проверка заказа самоката через нижнюю кнопку")  
    def test_successful_order_flow_bottom_button(self, driver):
        order_page = OrderPage(driver)
        order_page.go_to_site()
        order_page.close_cookie_banner()

        with allure.step("Начать заказ через нижнюю кнопку"):
            order_page.click_bottom_order_button()

        with allure.step("Заполнить первую страницу заказа"):
            order_page.fill_first_step_form(
                name=TestData.ORDER_DATA_2["name"],
                last_name=TestData.ORDER_DATA_2["last_name"],
                address=TestData.ORDER_DATA_2["address"],
                phone=TestData.ORDER_DATA_2["phone"],
                metro_station=TestData.ORDER_DATA_2["metro_station"]
            )

        with allure.step("Заполнить вторую страницу заказа"):
            order_page.fill_second_step_form(
                delivery_day=TestData.ORDER_DATA_2["delivery_day"],
                period=TestData.ORDER_DATA_2["period"],
                color=TestData.ORDER_DATA_2["color"],
                comment=TestData.ORDER_DATA_2["comment"]
            )

        with allure.step("Подтвердить заказ"):
            order_page.confirm_order()

        with allure.step("Проверить успешное оформление заказа"):
            success_message = order_page.get_success_message()
            assert "Заказ оформлен" in success_message