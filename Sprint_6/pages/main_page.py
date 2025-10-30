# main_page.py

from .base_page import BasePage
from locators import MainPageLocators
import allure


class MainPage(BasePage):
    
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = MainPageLocators

    @allure.step("Дождаться загрузки главной страницы")
    def wait_for_load_main_page(self):
        self.find_element(self.locators.ORDER_BUTTON_TOP)

    @allure.step("Кликнуть на вопрос {question_index}")
    def click_question(self, question_index):
        question = self.locators.QUESTION_LOCATORS[question_index]
        self.scroll_to_element(question)
        self.click_element(question)
        
        answer = self.locators.ANSWER_LOCATORS[question_index]
        self.wait_for_visibility(answer)

    @allure.step("Получить текст ответа {answer_index}")
    def get_answer_text(self, answer_index):
        answer = self.locators.ANSWER_LOCATORS[answer_index]
        element = self.find_element(answer)
        return element.text

    @allure.step("Кликнуть на верхнюю кнопку заказа")
    def click_order_button_top(self):
        self.click_element(self.locators.ORDER_BUTTON_TOP)

    @allure.step("Кликнуть на нижнюю кнопку заказа")
    def click_order_button_bottom(self):
        self.scroll_to_element(self.locators.ORDER_BUTTON_BOTTOM)
        self.click_element(self.locators.ORDER_BUTTON_BOTTOM)
    
    @allure.step("Кликнуть на логотип Самоката")
    def click_scooter_logo(self):
        self.click_element(self.locators.SCOOTER_LOGO)

    @allure.step("Кликнуть на логотип Яндекса")
    def click_yandex_logo(self):
        self.click_element(self.locators.YANDEX_LOGO)

    @allure.step("Проверить видимость верхней кнопки заказа")
    def is_order_button_top_visible(self):
        try:
            self.wait_for_visibility(self.locators.ORDER_BUTTON_TOP, time=3)
            return True
        except:
            return False