from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import unittest

class Simulator():
    def __init__(self, myDriver):
        self.driver = myDriver

        self.buy = (By.XPATH, '//div/a[@href="/Simulador/Comprar"]')
        self.symbol = (By.ID, 'search_symbol')
        self.quantity = (By.ID, 'Cantidad')
        self.quantity_field = (By.ID, 'ValorCantidad')
        self.limit_price = (By.ID, 'PrecioLimite')
        self.limit_price_field = (By.ID, 'ValorPrecioLimite')
        self.buy_button = (By.ID, 'btnComprar')
        self.password = (By.ID, 'Password')
        self.buy_conf = (By.ID, 'Submit')
        self.purchase_confiration = (By.XPATH, "//div[contains(.,'Su operación de compra virtual fue generada con éxito')]")

    def buy_stock(self, company, amount, max_price):
        actions = ActionChains(self.driver)
        self.driver.implicitly_wait(10)
        self.driver.find_element(*self.buy).click()
        self.driver.implicitly_wait(10)
        self.driver.find_element(*self.symbol).click()
        self.driver.find_element(*self.symbol).send_keys(company)
        self.driver.find_element(*self.symbol).send_keys(Keys.PAGE_DOWN)
        self.driver.find_element(*self.symbol).send_keys(Keys.ENTER)
        self.driver.find_element(*self.quantity).click()
        self.driver.find_element(*self.quantity_field).send_keys(amount)
        self.driver.find_element(*self.limit_price).click()
        self.driver.find_element(*self.limit_price_field).send_keys(max_price)
        self.driver.find_element(*self.buy_button).click()

    def confirm_buy(self,password):
        self.driver.find_element(*self.password).send_keys(password)
        self.driver.find_element(*self.buy_conf).click()

    def my_purchase_message_is_present(self):
        try:
            self.driver.find_element(*self.purchase_confiration)
        except NoSuchElementException:
            return False
        return True

    def check_purchase(self):
        self.driver.implicitly_wait(20)
        tc = unittest.TestCase('__init__')
        tc.assertTrue(self.my_purchase_message_is_present())






