from selenium.webdriver.common.by import By
from datetime import datetime
import time

class mailinator():
    def __init__(self, myDriver):
        self.driver = myDriver
        self.email = (By.ID, 'addOverlay')
        self.go = (By.ID, 'go-to-public')

    def look_for_email(self):
        self.driver.implicitly_wait(20)

        self.driver.find_element(*self.email).send_keys(datetime.now().strftime('%Y%m%d'+'v8'))
        self.driver.find_element(*self.go).click()


