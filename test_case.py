import pytest
from datetime import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

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
        check_user_info(user, driver)

        '''
        Логинимся менеджером, находим пользователя поиском и удаляем его
        В конце, чтобы удостовериться, ищем этого пользователя еще раз и проверяем, что он удалён
        '''
        case_page.logout()
        case_page.login_manager()
        case_page.search_and_delete(user)
        case_page.search(user)
        assert driver.find_element(By.XPATH, Locators.RESULT_TEXT).text == "Всего:0 "


# Сравнение всех полей в информации о пользователе
def check_user_info(user, driver):

    # Сначала преобразование дат в тот формат, в котором они хранятся на сайте
    user_birthday_datetime = datetime.strptime(str(user.birthday), '%d%m%Y')
    user_birthday_formatted = user_birthday_datetime.strftime('%Y-%m-%d')
    user_startday_datetime = datetime.strptime(str(user.startday), '%d%m%Y')
    user_startday_formatted = user_startday_datetime.strftime('%Y-%m-%d')

    assert driver.find_element(By.XPATH, Locators.USER_EMAIL).text == user.email
    assert driver.find_element(By.XPATH, Locators.USER_NAME).text == user.name
    assert driver.find_element(By.XPATH, Locators.USER_BIRTHDAY).text == user_birthday_formatted
    assert Select(driver.find_element(By.XPATH, Locators.USER_GENDER)).first_selected_option.text == user.gender
    assert driver.find_element(By.XPATH, Locators.USER_STARTDAY).text == user_startday_formatted
    assert driver.find_element(By.XPATH, Locators.USER_HOBBY).text == user.hobby
    assert driver.find_element(By.XPATH, Locators.USER_NAME1).text == user.name1
    assert driver.find_element(By.XPATH, Locators.USER_SURNAME1).text == user.surname1
    assert driver.find_element(By.XPATH, Locators.USER_FATHER1).text == user.father1
    assert driver.find_element(By.XPATH, Locators.USER_CAT).text == user.cat
    assert driver.find_element(By.XPATH, Locators.USER_DOG).text == user.dog
    assert driver.find_element(By.XPATH, Locators.USER_PARROT).text == user.parrot
    assert driver.find_element(By.XPATH, Locators.USER_CAVY).text == user.cavy
    assert driver.find_element(By.XPATH, Locators.USER_HAMSTER).text == user.hamster
    assert driver.find_element(By.XPATH, Locators.USER_SQUIRREL).text == user.squirrel
    assert driver.find_element(By.XPATH, Locators.USER_PHONE).text == user.phone
    assert driver.find_element(By.XPATH, Locators.USER_ADDRESS).text == user.address
    assert int(driver.find_element(By.XPATH, Locators.USER_INN).text) == user.inn