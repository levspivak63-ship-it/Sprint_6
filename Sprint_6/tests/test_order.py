import pytest
import allure
from pages.order_page import OrderPage


@allure.title("Проверка позитивного сценария заказа самоката через {order_button} кнопку")
@pytest.mark.parametrize("order_button,test_data", [
    ("верхнюю", {
        "name": "Иван",
        "last_name": "Петров",
        "address": "ул. Ленина, д. 1",
        "phone": "89991234567",
        "metro_station": "Бульвар Рокоссовского",
        "delivery_day": 15,
        "period": "сутки",
        "color": "black",
        "comment": "Первый тестовый заказ через верхнюю кнопку"
    }),
    ("нижнюю", {
        "name": "Мария",
        "last_name": "Сидорова",
        "address": "пр. Мира, д. 10",
        "phone": "89997654321",
        "metro_station": "Выхино",
        "delivery_day": 25,
        "period": "двое суток",
        "color": "grey",
        "comment": "Второй тестовый заказ через нижнюю кнопку"
    })
])
def test_successful_order_flow(driver, order_button, test_data):
    order_page = OrderPage(driver)
    order_page.go_to_site()

    with allure.step(f"1. Начало заказа через {order_button} кнопку"):
        if order_button == "верхнюю":
            order_page.click_top_order_button()
        else:
            order_page.click_bottom_order_button()

    with allure.step("2. Заполнение первой страницы заказа (личные данные)"):
        order_page.fill_first_step_form(
            name=test_data["name"],
            last_name=test_data["last_name"],
            address=test_data["address"],
            phone=test_data["phone"],
            metro_station=test_data["metro_station"]
        )

    with allure.step("3. Заполнение второй страницы заказа (данные аренды)"):
        order_page.fill_second_step_form(
            delivery_day=test_data["delivery_day"],
            period=test_data["period"],
            color=test_data["color"],
            comment=test_data["comment"]
        )

    with allure.step("4. Подтверждение заказа"):
        order_page.confirm_order()

    with allure.step("5. Проверка успешного оформления заказа"):
        success_message = order_page.get_success_message()
        assert "Заказ оформлен" in success_message