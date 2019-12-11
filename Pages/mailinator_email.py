from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.action_chains import ActionChains

class mailinator_email():
    def __init__(self, myDriver):
        self.driver = myDriver
        self.verificacion = (By.XPATH, "//td[contains(.,'no-reply@invertironline.com')]")
        self.validation_btn = (By.CSS_SELECTOR, ".button-td > .button-a")

    def validation(self):
        print('buscando')
        self.driver.find_element(*self.verificacion).click()
        asd = self.driver.find_element_by_tag_name("iframe")
        self.driver.switch_to.frame(asd)

        element = self.driver.find_element(*self.validation_btn)
        actions = ActionChains(self.driver)
        actions.move_to_element(element).click()
        time.sleep(3)
        #self.driver.find_element(*self.validation_btn).click()
        print('que ondaaa')
        time.sleep(3)

