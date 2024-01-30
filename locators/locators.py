from selenium.webdriver.common.by import By

# Экран авторизации
LOGIN = (By.XPATH, "/html/body/div[2]/div/ul/li[2]/a/span")
EMAIL = (By.NAME, "login")
PASSWORD = (By.NAME, "password")
AUTH_BUTTON = (By.XPATH, "/html/body/div[3]/div[1]/div[1]/form/table/tbody/tr[3]/td[2]/input")

# Экран создания нового юзера
ADD_USER = (By.XPATH, "/html/body/div[3]/p[1]/a")
NEW_NAME = (By.NAME, "noibiz_name")
NEW_EMAIL = (By.NAME, "noibiz_email")
NEW_PASS = (By.NAME, "noibiz_password")
ADD_USER_BUTTON = (By.NAME, "act_create")

USER_DROPDOWN = (By.CLASS_NAME, "dropdown-toggle")
LOGOUT = (By.XPATH, "/html/body/div[1]/div[2]/ul/li[3]/ul/li[3]/a")

# Экран поиска юзеров
SEARCH_FIELD = (By.NAME, "q")
SEARCH_BUTTON = (By.XPATH, "/html/body/div[3]/form/table/tbody/tr[5]/td[1]/button")
DETAILS_BUTTON = (By.XPATH, "/html/body/div[3]/table/tbody/tr/td[7]/a")
USER_EMAIL = "/html/body/div[3]/div[1]/div/div[2]/table/tbody/tr[1]/td[2]"
USER_NAME = "/html/body/div[3]/div[1]/div/div[2]/table/tbody/tr[2]/td[2]"
DELETE_BUTTON = (By.XPATH, "/html/body/div[3]/table/tbody/tr/td[6]/a")
RESULT_TEXT = "/html/body/div[3]/p[2]"
