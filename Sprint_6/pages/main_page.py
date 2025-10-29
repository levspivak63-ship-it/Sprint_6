from selenium.webdriver.common.by import By
from .base_page import BasePage


class MainPage(BasePage):
    
    QUESTION_LOCATORS = [
        (By.ID, "accordion__heading-0"),
        (By.ID, "accordion__heading-1"), 
        (By.ID, "accordion__heading-2"),
        (By.ID, "accordion__heading-3"),
        (By.ID, "accordion__heading-4"),
        (By.ID, "accordion__heading-5"),
        (By.ID, "accordion__heading-6"),
        (By.ID, "accordion__heading-7")
    ]
    
    ANSWER_LOCATORS = [
        (By.ID, "accordion__panel-0"),
        (By.ID, "accordion__panel-1"),
        (By.ID, "accordion__panel-2"), 
        (By.ID, "accordion__panel-3"),
        (By.ID, "accordion__panel-4"),
        (By.ID, "accordion__panel-5"),
        (By.ID, "accordion__panel-6"),
        (By.ID, "accordion__panel-7")
    ]
    
    ORDER_BUTTON_TOP = (By.XPATH, "//button[@class='Button_Button__ra12g']")
    ORDER_BUTTON_BOTTOM = (By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM']")
    
    SCOOTER_LOGO = (By.XPATH, "//a[@class='Header_LogoScooter__3lsAR']")
    YANDEX_LOGO = (By.XPATH, "//a[@class='Header_LogoYandex__3TSOI']")

    # ожидание загрузки главной страницы
    def wait_for_load_main_page(self):
        self.find_element(self.ORDER_BUTTON_TOP)

    # клик по вопросу о главном
    def click_question(self, question_index):
        question = self.QUESTION_LOCATORS[question_index]
        self.scroll_to_element(question)
        self.click_element(question)
        answer = self.ANSWER_LOCATORS[question_index]
        self.wait_for_visibility(answer)

    # ответ на вопрос о главном
    def get_answer_text(self, answer_index):
        answer = self.ANSWER_LOCATORS[answer_index]
        element = self.find_element(answer)
        return element.text

    # клик по верней кнопке "Заказать"
    def click_order_button_top(self):
        self.click_element(self.ORDER_BUTTON_TOP)

    # скролл до нижней кнопки "Заказать" и клик по ней
    def click_order_button_bottom(self):
        self.scroll_to_element(self.ORDER_BUTTON_BOTTOM)
        self.click_element(self.ORDER_BUTTON_BOTTOM)
    
    # клик по логотипу Скутер
    def click_scooter_logo(self):
        self.click_element(self.SCOOTER_LOGO)

    # клик по логотупу Яндекс
    def click_yandex_logo(self):
        self.click_element(self.YANDEX_LOGO)