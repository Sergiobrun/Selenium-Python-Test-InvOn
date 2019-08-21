from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import unittest
from datetime import datetime

class Home():
    def __init__(self, myDriver):
        self.driver = myDriver
        self.register = (By.XPATH, "//a[contains(.,'Registrarse')]")
        self.messages = (By.XPATH, '//li/a[@href="/User/MisMensajes"]')
        self.login_button = (By.XPATH, "//a[contains(.,'Ingresar')]")
        self.user = (By.ID,'username')
        self.password = (By.ID, 'password')
        self.login_2nd_button = (By.ID, 'sendlogin')

    def click_register_link(self):
        self.driver.find_element(*self.register).click()

    def my_messages_are_present(self):
        try:
            self.driver.find_element(*self.messages)
        except NoSuchElementException:
            return False
        return True

    def login(self, user, password):
        self.driver.find_element(*self.login_button).click()
        self.driver.find_element(*self.user).send_keys(user)
        self.driver.find_element(*self.password).send_keys(password)
        self.driver.find_element(*self.login_2nd_button).click()

    def check_login(self):
        self.driver.implicitly_wait(20)
        tc = unittest.TestCase('__init__')
        tc.assertTrue(self.my_messages_are_present())

