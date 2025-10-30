# locators.py
from selenium.webdriver.common.by import By


class MainPageLocators:
    # Вопросы о важном - оставляем как было
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
    
    # Кнопки заказа
    ORDER_BUTTON_TOP = (By.XPATH, "//button[@class='Button_Button__ra12g']")
    ORDER_BUTTON_BOTTOM = (By.XPATH, "(//button[contains(text(), 'Заказать')])[2]")
    
    # Логотипы
    SCOOTER_LOGO = (By.XPATH, "//a[@class='Header_LogoScooter__3lsAR']")
    YANDEX_LOGO = (By.XPATH, "//a[@class='Header_LogoYandex__3TSOI']")


class OrderPageLocators:
       
    # Первая страница формы
    NAME = (By.XPATH, "//input[@placeholder='* Имя']")
    LAST_NAME = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS_OF_DELIVERY = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_STATION = (By.XPATH, "//input[@placeholder='* Станция метро']")
    PHONE = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH, "//button[text()='Далее']")
    
    # Вторая страница формы
    DATE_OF_DELIVERY = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    RENTAL_PERIOD = (By.XPATH, "//div[contains(@class, 'Dropdown-root')]")
    COMMENT_INPUT = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    ORDER_BUTTON_SECOND_PAGE = (By.XPATH, "//div[contains(@class, 'Order_Content')]//button[text()='Заказать']")
    
    # Модальное окно
    MODAL_LOCATOR = (By.XPATH, "//div[contains(@class, 'Order_Modal')]")
    CONFIRM_ORDER_BUTTON = (By.XPATH, "//div[contains(@class, 'Order_Modal')]//button[text()='Да']")
    SUCCESS_MESSAGE = (By.XPATH, "//div[contains(@class, 'Order_ModalHeader')]")
    
    # Опции
    RENTAL_PERIOD_OPTION_ONE_DAY = (By.XPATH, "//div[text()='сутки']")
    RENTAL_PERIOD_OPTION_TWO_DAYS = (By.XPATH, "//div[text()='двое суток']")
    COLOR_BLACK_CHECKBOX = (By.ID, "black")
    COLOR_GREY_CHECKBOX = (By.ID, "grey")
    
    # Календарь и метро
    CALENDAR_MODAL = (By.CLASS_NAME, "react-datepicker")
    METRO_FIRST_OPTION = (By.XPATH, "//button[contains(@class, 'select-search__option')][1]")


class CommonLocators:
    # Общие локаторы
    COOKIE_BANNER = (By.XPATH, "//button[contains(text(), 'да все привыкли')]")