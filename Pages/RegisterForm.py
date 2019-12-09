from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class Register_form():
    def __init__(self, myDriver):
        self.driver = myDriver
        self.name = (By.ID, 'nombre')
        self.last_name = (By.ID, 'apellido')
        self.email = (By.ID, 'email')
        self.conf_email = (By.ID, 'confirmacion-email')
        self.username = (By.ID, 'Username')
        self.password = (By.ID, 'password')
        self.conf_password = (By.ID, 'confirmacion-password')
        self.province = (By.ID, 'SeleccProv')
        self.phone_prefix = (By.ID, 'prefijo-telefono')
        self.phone = (By.ID, 'numero-telefono')
        self.terms = (By.ID, 'TermsAndConditions')
        self.register_button = (By.ID, 'registrar-btn')


    def fill_fields(self, name, last_name, email, password, prefix, phone):
        self.driver.implicitly_wait(20)
        self.driver.find_element(*self.name).send_keys(name)
        self.driver.find_element(*self.last_name).send_keys(last_name)
        self.driver.find_element(*self.email).send_keys(email)
        self.driver.find_element(*self.conf_email).send_keys(email)
        #self.driver.find_element(*self.username).send_keys(user)
        self.driver.find_element(*self.password).send_keys(password)
        self.driver.find_element(*self.conf_password).send_keys(password)
        #Select(self.driver.find_element(*self.province)).select_by_visible_text(province)
        self.driver.find_element(*self.phone_prefix).send_keys(prefix)
        self.driver.find_element(*self.phone).send_keys(phone)
        #self.driver.find_element(*self.terms).click()
        self.driver.find_element(*self.register_button).click()