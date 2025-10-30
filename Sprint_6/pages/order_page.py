# order_page.py

from selenium.webdriver.common.by import By
from .base_page import BasePage
from locators import OrderPageLocators, MainPageLocators
import allure


class OrderPage(BasePage):
    
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = OrderPageLocators
        self.main_locators = MainPageLocators

    @allure.step("Дождаться загрузки страницы заказа")
    def wait_for_load_order_page(self):
        self.wait_for_order_page()
        self.find_element(self.locators.NAME)

    @allure.step("Кликнуть на верхнюю кнопку заказа")
    def click_top_order_button(self):
        self.click_element(self.main_locators.ORDER_BUTTON_TOP)
        self.wait_for_load_order_page()

    @allure.step("Кликнуть на нижнюю кнопку заказа")
    def click_bottom_order_button(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.wait_for_visibility(self.main_locators.ORDER_BUTTON_BOTTOM)
        self.click_element(self.main_locators.ORDER_BUTTON_BOTTOM)
        self.wait_for_load_order_page()

    @allure.step("Выбрать станцию метро {station_name}")
    def select_metro_station(self, station_name):
        metro_input = self.find_element(self.locators.METRO_STATION)
        self.scroll_to_element(self.locators.METRO_STATION)
        metro_input.click()
        metro_input.clear()
        metro_input.send_keys(station_name)
        self.wait_for_clickable(self.locators.METRO_FIRST_OPTION).click()

    @allure.step("Выбрать дату доставки {day_number}")
    def select_delivery_date_from_calendar(self, day_number):
        self.click_element(self.locators.DATE_OF_DELIVERY)
        self.wait_for_visibility(self.locators.CALENDAR_MODAL)
        day_locator = (By.XPATH, f"//div[text()='{day_number}']")
        self.click_element(day_locator)

    @allure.step("Выбрать период аренды {period}")
    def select_rental_period(self, period):
        self.click_element(self.locators.RENTAL_PERIOD)
        if period == "сутки":
            self.click_element(self.locators.RENTAL_PERIOD_OPTION_ONE_DAY)
        elif period == "двое суток":
            self.click_element(self.locators.RENTAL_PERIOD_OPTION_TWO_DAYS)

    @allure.step("Выбрать цвет самоката {color}")
    def select_scooter_color(self, color):
        if color == "black":
            self.click_element(self.locators.COLOR_BLACK_CHECKBOX)
        elif color == "grey":
            self.click_element(self.locators.COLOR_GREY_CHECKBOX)

    @allure.step("Заполнить первую страницу формы заказа")
    def fill_first_step_form(self, name, last_name, address, phone, metro_station):
        self.find_element(self.locators.NAME).send_keys(name)
        self.find_element(self.locators.LAST_NAME).send_keys(last_name)
        self.find_element(self.locators.ADDRESS_OF_DELIVERY).send_keys(address)
        self.select_metro_station(metro_station)
        
        phone_field = self.find_element(self.locators.PHONE)
        phone_field.clear()
        phone_field.send_keys(phone)
        
        self.click_element(self.locators.NEXT_BUTTON)
        self.wait_for_visibility(self.locators.DATE_OF_DELIVERY)

    @allure.step("Заполнить вторую страницу формы заказа")
    def fill_second_step_form(self, delivery_day, period="сутки", color="black", comment=""):
        self.select_delivery_date_from_calendar(delivery_day)
        self.select_rental_period(period)
        self.select_scooter_color(color)
        
        if comment:
            self.find_element(self.locators.COMMENT_INPUT).send_keys(comment)
        
        self.scroll_to_element(self.locators.ORDER_BUTTON_SECOND_PAGE)
        self.click_element(self.locators.ORDER_BUTTON_SECOND_PAGE)
        self.wait_for_visibility(self.locators.MODAL_LOCATOR)

    @allure.step("Подтвердить заказ")
    def confirm_order(self):
        self.click_element(self.locators.CONFIRM_ORDER_BUTTON)
        self.wait_for_visibility(self.locators.SUCCESS_MESSAGE)

    @allure.step("Получить сообщение об успехе")
    def get_success_message(self):
        element = self.find_element(self.locators.SUCCESS_MESSAGE)
        return element.text

    @allure.step("Проверить наличие сообщения об успешном заказе")
    def is_success_message_displayed(self):
        try:
            self.wait_for_visibility(self.locators.SUCCESS_MESSAGE, time=3)
            return True
        except:
            return False