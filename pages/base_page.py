from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class BasePage:

    def __init__(self, driver, url="http://users.bugred.ru"):
        self.driver = driver
        self.url = url

    def open(self):
        self.driver.get(self.url)

    def element_is_visible(self, locator, timeout=10):
        return Wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))