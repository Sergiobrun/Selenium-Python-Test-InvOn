from Pages.Home import *
from Pages.RegisterForm import *
from Pages.Simulator import *
from Pages.mailinator import *
from Pages.mailinator_email import *
from Pages.Login import *
from datetime import datetime
from selenium.webdriver.chrome.options import Options
import HtmlTestRunner
import sys

class TestInvOnlie(unittest.TestCase):

    def setUp(self):
        options = Options()
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        if sys.platform == 'win32':
            self.driver = webdriver.Chrome('chromedriver.exe', chrome_options=options)
        elif sys.platform == 'linux':
            self.driver = webdriver.Chrome('chromedriver')
        self.driver.get('https://www.invertironline.com/')
        self.home = Home(self.driver)
        self.mailinator = mailinator(self.driver)
        self.mailinator_email = mailinator_email(self.driver)
        self.register = Register_form(self.driver)
        self.simulator = Simulator(self.driver)
        self.login = Login(self.driver)
        self.email = str(datetime.now().strftime('%Y%m%d' + 'v8'+ '@mailinator.com'))
        self.user = str(datetime.now().strftime('User'+'%Y%m%d'))
        self.password = str(datetime.now().strftime('Pass'+'%Y%m%d'))


    def test_new_account(self):
        self.home.click_register_link()
        self.register.fill_fields('Sergio','Bruno',self.email, self.password,'261', '1234567')
        self.driver.get('https://www.mailinator.com/')
        self.mailinator.look_for_email()
        self.mailinator_email.validation()
        self.driver.get('https://micuenta.invertironline.com/ingresar?url=https://www.invertironline.com/&intencion=0')
        self.login.login(self.email, self.password)
        self.home.check_login()

    '''
    def test_buy_sim_stocks(self):
        self.home.login(self.email, self.password)
        self.simulator.buy_stock('YPFD','2','620')
        self.simulator.confirm_buy(self.password)
        self.simulator.check_purchase()
    '''
#asd
    def tearDown(self):
        self.driver.close()
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(testRunner= HtmlTestRunner.HTMLTestRunner(output='myreport'))
    unittest.main()
