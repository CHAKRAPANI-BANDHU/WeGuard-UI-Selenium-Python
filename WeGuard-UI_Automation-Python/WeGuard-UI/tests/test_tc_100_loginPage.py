from datetime import datetime
import pytest
from pageObjects.loginpage import LoginPage
from testData.loginpagedata import LoginPageData
from tests.conftest import driver
from utilities.baseClass import BaseClass
import WeGuardlogger as WeGuard
import Executor as Configs
import time
#from castro import Castro

# The flow for login function is defined in test_login class
class TestLoginPage(BaseClass):
    @pytest.mark.skipif(Configs.test_tc_001_User_login == 0, reason= "Login with Valid Credentials is skipped")
    @pytest.mark.run(order=101)
    def test_tc_101_Login(self, getData):
     WeGuard.logger.debug("\n\n--------------------------- Login Start ---------------------------\n\n")
     try:
            self.wait()
            loginPage = LoginPage(self.driver)
#           self.disableCookies()
            WeGuard.logger.debug("Username : " + getData["username"])
            loginPage.getUserName().send_keys(getData["username"])
            WeGuard.logger.debug("Password : " + getData["password"])
            loginPage.getPassword().send_keys(getData["password"])
            loginPage.getrememberPassword().click()
            loginPage.getLoginButton().click()
            # alertmessage = loginPage.getAlertMessage().text
            # assert alertmessage == getData["alert"]
            now1 = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            self.driver.get_screenshot_as_file('Passed_Testcases_Screenshots/screenshot-%s.png' % now1)
            WeGuard.logger.debug("\n\n--------------------------- Login Pass ---------------------------\n\n")
            time.sleep(60)
           # self.driver.refresh()
           # self.driver.quit()
     except BaseException as e:
            WeGuard.logger.error('Error at %s', 'BaseException', exc_info=e)
            WeGuard.logger.error("\n\n--------------------------- Login Fail ---------------------------\n\n")
            WeGuard.logger.error("Exception : " + str(e))
            now2 = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            self.driver.get_screenshot_as_file('Failed_Testcases_Screenshots/screenshot-%s.png' % now2)
            assert False

    def tearDownClass(self, cls):
           driver.close()
           driver.quit()
           #self.screenCapture.stop();

    # Test data is fetched from getData function
    @pytest.fixture(params=LoginPageData.test_LoginPageData)
    def getData(self, request):
        return request.param
