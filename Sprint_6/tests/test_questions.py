import pytest
import allure
from pages.main_page import MainPage


class TestQuestions:
    
    @allure.title("Проверка ответов на вопросы в разделе 'Вопросы о важном'")
    @pytest.mark.parametrize("question_index", [0, 1, 2, 3, 4, 5, 6, 7])
    def test_question_answers(self, driver, question_index):
        main_page = MainPage(driver)
        main_page.go_to_site()
        
        with allure.step(f"Клик на вопрос {question_index}"):
            main_page.click_question(question_index)
        
        with allure.step(f"Проверка открытия ответа {question_index}"):
            answer_locator = main_page.ANSWER_LOCATORS[question_index]
            main_page.wait_for_visibility(answer_locator)
            
            actual_answer = main_page.get_answer_text(question_index)
            assert actual_answer