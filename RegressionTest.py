from Pages.Home import *
from Pages.RegisterForm import *
from Pages.Simulator import *
from datetime import datetime
from selenium.webdriver.chrome.options import Options
import xmlrunner

class TestInvOnlie(unittest.TestCase):

    def setUp(self):
        options = Options()
        options.headless = True
        self.driver = webdriver.Chrome('chromedriver.exe', chrome_options = options)
        self.driver.get('https://www.invertironline.com/')
        self.home = Home(self.driver)
        self.register = Register_form(self.driver)
        self.simulator = Simulator(self.driver)
        self.email = str(datetime.now().strftime('%Y%m%d' + '@mailinator.com'))
        self.user = str(datetime.now().strftime('User'+'%Y%m%d'))
        self.password = str(datetime.now().strftime('Pass'+'%Y%m%d'))

    def test_new_account(self):
        self.home.click_register_link()
        self.register.fill_fields('Sergio','Brun',self.email, self.user, self.password, 'Mendoza','261', '1234567')
        self.home.check_login()

    def test_buy_sim_stocks(self):
        self.home.login(self.email, self.password)
        self.simulator.buy_stock('YPFD','2','620')
        self.simulator.confirm_buy(self.password)
        self.simulator.check_purchase()

    def tearDown(self):
        self.driver.close()
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='myreport'))
    unittest.main()
