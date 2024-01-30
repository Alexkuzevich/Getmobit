import pytest
from selenium.webdriver.common.by import By
from conftest import driver
import locators.locators as Locators
from pages.main_page import MainPage


@pytest.mark.usefixtures('driver')
class TestCase:

    def test_case(self, driver):

        case_page = MainPage(driver)
        case_page.open()

        # Под менеджером создаем нового пользователя, заполнив все поля
        case_page.login_manager()
        user = case_page.create_new_user()
        case_page.logout()

        '''
        Логинимся новым пользователем
        В списке пользователей находим пользователя поиском и нажимаем на нем кнопку Посмотреть
        Сравниваем те поля, что тут отображаются, с введенными при создании
        '''
        case_page.login(user)
        case_page.search_and_info(user)
        assert driver.find_element(By.XPATH, Locators.USER_EMAIL).text == user.email
        assert driver.find_element(By.XPATH, Locators.USER_NAME).text == user.name

        '''
        Логинимся менеджером, находим пользователя поиском и удаляем его
        В конце, чтобы удостовериться, ищем этого пользователя еще раз и проверяем, что он удалён
        '''
        case_page.logout()
        case_page.login_manager()
        case_page.search_and_delete(user)
        case_page.search(user)
        assert driver.find_element(By.XPATH, Locators.RESULT_TEXT).text == "Всего:0 "

