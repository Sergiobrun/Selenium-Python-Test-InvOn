from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

class Login():
    def __init__(self, myDriver):
        self.driver = myDriver
        self.email = (By.ID,'usuario')
        self.passw = (By.ID, 'password')
        self.reg = (By.XPATH, '//input[contains(@class, "btn btn-primary px-5")]')

    def login(self, email, passw):
        self.driver.find_element(*self.email).send_keys(email)
        self.driver.find_element(*self.passw).send_keys(passw)
        self.driver.find_element(*self.reg).click()
        time.sleep(3)
