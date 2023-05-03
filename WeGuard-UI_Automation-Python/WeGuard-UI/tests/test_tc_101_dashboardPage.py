from datetime import datetime

import pytest
from pageObjects.dashboardpage import DashboardPage
from testData.dashboardpagedata import DashboardPageData
from utilities.baseClass import BaseClass
import WeGuardlogger as WeGuard
import Executor as Configs
import time

# The flow for login function is defined in test_login class
class TestDashboardPage(BaseClass):
    @pytest.mark.skipif(Configs.test_tc_002_User_dashboard == 0, reason="Dashboard page is skipped")
    @pytest.mark.run(order=101)
    def test_tc_102_Dashboard(self, getData):
     WeGuard.logger.debug("\n\n--------------------------- Dashboard Start ---------------------------\n\n")
     try:
            self.driver.wait()
            dashboardPage = DashboardPage(self.driver)
            WeGuard.logger.debug("Active Users: " + getData["ActiveUsers"])
            print(dashboardPage.getActiveUsers())
            WeGuard.logger.debug("Active Users Count: " + getData["ActiveUsersCount"])
            print(dashboardPage.getActiveUsersCount())
            now1 = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            self.driver.get_screenshot_as_file('Passed_Testcases_Screenshots/screenshot-%s.png' % now1)
            WeGuard.logger.debug("\n\n--------------------------- Dashboard Pass ---------------------------\n\n")
            time.sleep(60)
            self.driver.refresh()
     except BaseException as e:
            WeGuard.logger.error('Error at %s', 'BaseException', exc_info=e)
            now2 = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            self.driver.get_screenshot_as_file('Failed_Testcases_Screenshots/screenshot-%s.png' % now2)
            WeGuard.logger.error("\n\n--------------------------- Dashboard Fail ---------------------------\n\n")
            WeGuard.logger.error("Exception : " + str(e))
            assert False

    # Test data is fetched from getData function
    @pytest.fixture(params=DashboardPageData.test_DashboardPageData)
    def getData(self, request):
        return request.param