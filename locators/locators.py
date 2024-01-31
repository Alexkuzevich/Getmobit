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
NEW_BIRTHDAY = (By.NAME, "noibiz_birthday")
NEW_GENDER = (By.NAME, "noibiz_gender")
NEW_STARTDAY = (By.NAME, "noibiz_date_start")
NEW_HOBBY = (By.NAME, "noibiz_hobby")
NEW_NAME1 = (By.NAME, "noibiz_name1")
NEW_SURNAME1 = (By.NAME, "noibiz_surname1")
NEW_FATHER1 = (By.XPATH, "/html/body/div[3]/form/table/tbody/tr[11]/td[2]/input[1]")
NEW_CAT = (By.NAME, "noibiz_cat")
NEW_DOG = (By.NAME, "noibiz_dog")
NEW_PARROT = (By.NAME, "noibiz_parrot")
NEW_CAVY = (By.NAME, "noibiz_cavy")
NEW_HAMSTER = (By.NAME, "noibiz_hamster")
NEW_SQUIRREL = (By.NAME, "noibiz_squirrel")
NEW_PHONE = (By.NAME, "noibiz_phone")
NEW_ADDRESS = (By.NAME, "noibiz_adres")
NEW_INN = (By.NAME, "noibiz_inn")
ADD_USER_BUTTON = (By.NAME, "act_create")

USER_DROPDOWN = (By.CLASS_NAME, "dropdown-toggle")
LOGOUT = (By.XPATH, "/html/body/div[1]/div[2]/ul/li[3]/ul/li[3]/a")

# Экран поиска юзеров + экран подробной информации о юзере
SEARCH_FIELD = (By.NAME, "q")
SEARCH_BUTTON = (By.XPATH, "/html/body/div[3]/form/table/tbody/tr[5]/td[1]/button")
DETAILS_BUTTON = (By.XPATH, "/html/body/div[3]/table/tbody/tr/td[7]/a")
USER_EMAIL = "/html/body/div[3]/div[1]/div/div[2]/table/tbody/tr[1]/td[2]"
USER_NAME = "/html/body/div[3]/div[1]/div/div[2]/table/tbody/tr[2]/td[2]"
USER_BIRTHDAY = "/html/body/div[3]/div[1]/div/div[2]/table/tbody/tr[4]/td[2]"
USER_GENDER = "/html/body/div[3]/div[1]/div/div[2]/table/tbody/tr[3]/td[2]/select"
USER_STARTDAY = "/html/body/div[3]/div[1]/div/div[2]/table/tbody/tr[5]/td[2]"
USER_HOBBY = "/html/body/div[3]/div[1]/div/div[2]/table/tbody/tr[6]/td[2]/textarea"
USER_NAME1 = "/html/body/div[3]/div[1]/div/div[2]/table/tbody/tr[7]/td[2]"
USER_SURNAME1 = "/html/body/div[3]/div[1]/div/div[2]/table/tbody/tr[8]/td[2]"
USER_FATHER1 = "/html/body/div[3]/div[1]/div/div[2]/table/tbody/tr[9]/td[2]"
USER_CAT = "/html/body/div[3]/div[1]/div/div[2]/table/tbody/tr[10]/td[2]"
USER_DOG = "/html/body/div[3]/div[1]/div/div[2]/table/tbody/tr[11]/td[2]"
USER_PARROT = "/html/body/div[3]/div[1]/div/div[2]/table/tbody/tr[12]/td[2]"
USER_CAVY = "/html/body/div[3]/div[1]/div/div[2]/table/tbody/tr[13]/td[2]"
USER_HAMSTER = "/html/body/div[3]/div[1]/div/div[2]/table/tbody/tr[14]/td[2]"
USER_SQUIRREL = "/html/body/div[3]/div[1]/div/div[2]/table/tbody/tr[15]/td[2]"
USER_PHONE = "/html/body/div[3]/div[1]/div/div[2]/table/tbody/tr[16]/td[2]"
USER_ADDRESS = "/html/body/div[3]/div[1]/div/div[2]/table/tbody/tr[17]/td[2]"
USER_INN = "/html/body/div[3]/div[1]/div/div[2]/table/tbody/tr[18]/td[2]"
DELETE_BUTTON = (By.XPATH, "/html/body/div[3]/table/tbody/tr/td[6]/a")
RESULT_TEXT = "/html/body/div[3]/p[2]"
