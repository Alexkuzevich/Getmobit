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
