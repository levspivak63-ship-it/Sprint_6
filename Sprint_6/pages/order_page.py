from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage


class OrderPage(BasePage):
    
    TOP_ORDER_BUTTON = (By.XPATH, "//button[@class='Button_Button__ra12g']")
    BOTTOM_ORDER_BUTTON = (By.XPATH, "(//button[contains(text(), 'Заказать')])[2]")
    
    NAME = (By.XPATH, "//input[@placeholder='* Имя']")
    LAST_NAME = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS_OF_DELIVERY = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_STATION = (By.XPATH, "//input[@placeholder='* Станция метро']")
    PHONE = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH, "//button[text()='Далее']")
    
    DATE_OF_DELIVERY = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    RENTAL_PERIOD = (By.XPATH, "//div[contains(@class, 'Dropdown-root')]")
    COMMENT_INPUT = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    ORDER_BUTTON_SECOND_PAGE = (By.XPATH, "//div[contains(@class, 'Order_Content')]//button[text()='Заказать']")
    
    MODAL_LOCATOR = (By.XPATH, "//div[contains(@class, 'Order_Modal')]")
    CONFIRM_ORDER_BUTTON = (By.XPATH, "//div[contains(@class, 'Order_Modal')]//button[text()='Да']")
    SUCCESS_MESSAGE = (By.XPATH, "//div[contains(@class, 'Order_ModalHeader')]")
    
    RENTAL_PERIOD_OPTION_ONE_DAY = (By.XPATH, "//div[text()='сутки']")
    RENTAL_PERIOD_OPTION_TWO_DAYS = (By.XPATH, "//div[text()='двое суток']")
    COLOR_BLACK_CHECKBOX = (By.ID, "black")
    COLOR_GREY_CHECKBOX = (By.ID, "grey")
    
    CALENDAR_MODAL = (By.CLASS_NAME, "react-datepicker")
    CALENDAR_DAY = (By.CLASS_NAME, "react-datepicker__day")
    CALENDAR_TODAY = (By.CSS_SELECTOR, ".react-datepicker__day--today")
    
    METRO_FIRST_OPTION = (By.XPATH, "//button[contains(@class, 'select-search__option')][1]")

    def wait_for_load_order_page(self):
        self.find_element(self.NAME)

    def click_top_order_button(self):
        self.click_element(self.TOP_ORDER_BUTTON)
        self.wait_for_load_order_page()

    def click_bottom_order_button(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        
        import time
        time.sleep(2)
        
        self.click_element(self.BOTTOM_ORDER_BUTTON)
        self.wait_for_load_order_page()

    def select_metro_station(self, station_name):
        metro_input = self.find_element(self.METRO_STATION)
        self.scroll_to_element(self.METRO_STATION)
        metro_input.click()
        metro_input.clear()
        metro_input.send_keys(station_name)
        
        self.wait_for_clickable(self.METRO_FIRST_OPTION).click()

    def select_delivery_date_from_calendar(self, day_number):
        self.click_element(self.DATE_OF_DELIVERY)
        
        self.wait_for_visibility(self.CALENDAR_MODAL)
        
        day_locator = (By.XPATH, f"//div[text()='{day_number}']")
        self.click_element(day_locator)

    def select_rental_period(self, period):
        self.click_element(self.RENTAL_PERIOD)
        if period == "сутки":
            self.click_element(self.RENTAL_PERIOD_OPTION_ONE_DAY)
        elif period == "двое суток":
            self.click_element(self.RENTAL_PERIOD_OPTION_TWO_DAYS)

    def select_scooter_color(self, color):
        if color == "black":
            self.click_element(self.COLOR_BLACK_CHECKBOX)
        elif color == "grey":
            self.click_element(self.COLOR_GREY_CHECKBOX)

    def fill_first_step_form(self, name, last_name, address, phone, metro_station):
        self.find_element(self.NAME).send_keys(name)
        self.find_element(self.LAST_NAME).send_keys(last_name)
        self.find_element(self.ADDRESS_OF_DELIVERY).send_keys(address)
        self.select_metro_station(metro_station)
        
        phone_field = self.find_element(self.PHONE)
        phone_field.clear()
        phone_field.send_keys(phone)
        
        self.click_element(self.NEXT_BUTTON)
        
        self.wait_for_visibility(self.DATE_OF_DELIVERY)

    def fill_second_step_form(self, delivery_day, period="сутки", color="black", comment=""):
        self.select_delivery_date_from_calendar(delivery_day)
        self.select_rental_period(period)
        self.select_scooter_color(color)
        
        if comment:
            self.find_element(self.COMMENT_INPUT).send_keys(comment)
        
        self.scroll_to_element(self.ORDER_BUTTON_SECOND_PAGE)
        self.click_element(self.ORDER_BUTTON_SECOND_PAGE)
        
        self.wait_for_visibility(self.MODAL_LOCATOR)

    def confirm_order(self):
        self.click_element(self.CONFIRM_ORDER_BUTTON)
        
        self.wait_for_visibility(self.SUCCESS_MESSAGE)

    def get_success_message(self):
        element = self.find_element(self.SUCCESS_MESSAGE)
        return element.text