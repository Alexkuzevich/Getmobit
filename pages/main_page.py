from selenium.webdriver.support.ui import Select
from pages.base_page import BasePage
import locators.locators as Locators
from generator.generator import generated_user


class MainPage(BasePage):

    # Логин под менеджером
    def login_manager(self):

        manager_mail = "manager@mail.ru"
        manager_password = "1"

        self.element_is_visible(Locators.LOGIN).click()
        self.element_is_visible(Locators.EMAIL).send_keys(manager_mail)
        self.element_is_visible(Locators.PASSWORD).send_keys(manager_password)
        self.element_is_visible(Locators.AUTH_BUTTON).click()

    # Создание нового пользователя
    def create_new_user(self):

        user = generated_user()
        self.element_is_visible(Locators.ADD_USER).click()
        self.element_is_visible(Locators.NEW_NAME).send_keys(user.name)
        self.element_is_visible(Locators.NEW_EMAIL).send_keys(user.email)
        self.element_is_visible(Locators.NEW_PASS).send_keys(user.password)
        self.element_is_visible(Locators.NEW_BIRTHDAY).send_keys(user.birthday)
        dropdown = self.element_is_visible(Locators.NEW_GENDER)
        gender = Select(dropdown)
        gender.select_by_index(1)
        self.element_is_visible(Locators.NEW_STARTDAY).send_keys(user.startday)
        self.element_is_visible(Locators.NEW_HOBBY).send_keys(user.hobby)
        self.element_is_visible(Locators.NEW_NAME1).send_keys(user.name1)
        self.element_is_visible(Locators.NEW_SURNAME1).send_keys(user.surname1)
        self.element_is_visible(Locators.NEW_FATHER1).send_keys(user.father1)
        self.element_is_visible(Locators.NEW_CAT).send_keys(user.cat)
        self.element_is_visible(Locators.NEW_DOG).send_keys(user.dog)
        self.element_is_visible(Locators.NEW_PARROT).send_keys(user.parrot)
        self.element_is_visible(Locators.NEW_CAVY).send_keys(user.cavy)
        self.element_is_visible(Locators.NEW_HAMSTER).send_keys(user.hamster)
        self.element_is_visible(Locators.NEW_SQUIRREL).send_keys(user.squirrel)
        self.element_is_visible(Locators.NEW_PHONE).send_keys(user.phone)
        self.element_is_visible(Locators.NEW_ADDRESS).send_keys(user.address)
        self.element_is_visible(Locators.NEW_INN).send_keys(user.inn)
        self.element_is_visible(Locators.ADD_USER_BUTTON).click()
        return user

    # Разлогин
    def logout(self):

        self.element_is_visible(Locators.USER_DROPDOWN).click()
        self.element_is_visible(Locators.LOGOUT).click()

    # Логин под обычным (созданным) юзером
    def login(self, user):

        self.element_is_visible(Locators.LOGIN).click()
        self.element_is_visible(Locators.EMAIL).send_keys(user.email)
        self.element_is_visible(Locators.PASSWORD).send_keys(user.password)
        self.element_is_visible(Locators.AUTH_BUTTON).click()

    # Поиск юзера и просмотр подробной информации о нём
    def search_and_info(self, user):

        self.element_is_visible(Locators.SEARCH_FIELD).send_keys(user.email)
        self.element_is_visible(Locators.SEARCH_BUTTON).click()
        self.element_is_visible(Locators.DETAILS_BUTTON).click()

    # Поиск юзера и его удаление
    def search_and_delete(self, user):

        self.element_is_visible(Locators.SEARCH_FIELD).send_keys(user.email)
        self.element_is_visible(Locators.SEARCH_BUTTON).click()
        self.element_is_visible(Locators.DELETE_BUTTON).click()

    # Поиск юзера (просто поиск)
    def search(self, user):

        self.element_is_visible(Locators.SEARCH_FIELD).send_keys(user.email)
        self.element_is_visible(Locators.SEARCH_BUTTON).click()
