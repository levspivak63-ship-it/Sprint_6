import pytest
import allure
from pages.order_page import OrderPage
from data import TestData


class TestOrder:
    
    @allure.title("Проверка заказа самоката")
    @pytest.mark.parametrize("click_method,test_data,scenario_name", [
        ("click_top_order_button", TestData.ORDER_DATA_1, "через верхнюю кнопку Заказать"),
        ("click_bottom_order_button", TestData.ORDER_DATA_2, "через нижнюю кнопку Заказать")
    ])
    def test_successful_order_flow(self, driver, click_method, test_data, scenario_name):
        order_page = OrderPage(driver)
        order_page.go_to_site()
        order_page.close_cookie_banner()

        with allure.step(f"Начать заказ {scenario_name}"):
            getattr(order_page, click_method)()

        with allure.step("Заполнить первую страницу заказа"):
            order_page.fill_first_step_form(
                name=test_data["name"],
                last_name=test_data["last_name"],
                address=test_data["address"],
                phone=test_data["phone"],
                metro_station=test_data["metro_station"]
            )

        with allure.step("Заполнить вторую страницу заказа"):
            order_page.fill_second_step_form(
                delivery_day=test_data["delivery_day"],
                period=test_data["period"],
                color=test_data["color"],
                comment=test_data["comment"]
            )

        with allure.step(f"Подтвердить заказ"):
            order_page.confirm_order()

        with allure.step(f"Проверить успешное оформление заказа {scenario_name}"):
            success_message = order_page.get_success_message()
            assert "Заказ оформлен" in success_message