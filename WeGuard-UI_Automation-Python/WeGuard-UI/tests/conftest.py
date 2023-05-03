import os
from datetime import datetime

import pytest
from selenium import webdriver
import variables as globalvar
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager
import WeGuardlogger as WeGuard
from selenium.webdriver.chrome.service import Service

driver = None

global path
# noinspection PyRedeclaration
path = os.getcwd()


# This method will make the user to select which browser to execute
def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )

# Browser executable paths and base settings
@pytest.fixture(scope="class")
def setup(request):
    global driver
    browser_name = request.config.getoption("browser_name")
    if browser_name.casefold() == "chrome":
        # Make sure that we are using the chrome options from webdriver manager
       # driver = globalvar.chrome_driver_path
        chromeOptions = webdriver.ChromeOptions()
        s = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=s)
        #driver = webdriver.Chrome(ChromeDriverManager().install(), options=chromeOptions)
        chromeOptions.add_argument("--start-maximized")
        params = {'behavior': 'allow', 'downloadPath': os.getcwd()}
        driver.execute_cdp_cmd('Page.setDownloadBehavior', params)
    elif browser_name.casefold() == "firefox":
        driver = webdriver.Firefox(GeckoDriverManager().install())
    elif browser_name.casefold() == "safari":  # For safari not required any executable file instead we need to enable the "Allow remote automation" from developer option to execute
        driver = webdriver.Safari()
    elif browser_name.casefold() == "ie":
        print("IE")
    driver.maximize_window()
    driver.get(globalvar.LoginUrl)
    driver.implicitly_wait(globalvar.wait)
    # This request will assign the driver object defined in this class to driver object used in the class where setup fixture is used
    request.cls.driver = driver
    yield
    driver.close()
    driver.quit()

@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    fullpath = path + "\\reports"
    if not os.path.exists(fullpath):
        os.makedirs(path + "\\reports")
        WeGuard.logger.debug("Full path of the reports is : " + fullpath)
    config.option.htmlpath = (
            "Reports/" + "Report_" + datetime.now().strftime("%d-%m-%Y %H-%M-%S") + ".html"
    )


def _capture_screenshot(self, name):
    # driver.snapshot(filepath)
      self.driver.get_screenshot_as_file(name)

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    pytest_html = item.config.pluginmanager.getplugin("html")
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, "extra", [])
    if report.when == "call":
        # always add url to report
        xfail = hasattr(report, "wasxfail")
        if (report.skipped and xfail) or (report.failed and not xfail):
            # only add additional html on failure
            now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            extra.append(pytest_html.extras.image("Reports/" + r"screenshots\image.png" % now))
            extra.append(pytest_html.extras.html("<div>Additional HTML</div>"))
        report.extra = extra


# @pytest.mark.hookwrapper
# def pytest_runtest_makereport(item):
#     """
#         Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
#         :param item:
#     """
#     pytest_html = item.config.pluginmanager.getplugin("html")
#     outcome = yield
#     report = outcome.get_result()
#     extra = getattr(report, "extra", [])
#     if report.when == "call" or report.when == "setup":
#         xfail = hasattr(report, "wasxfail")
#         if (report.skipped and xfail) or (report.failed and not xfail):
#             WeGuard.logger.debug("The OS path is : " + path)
#             filepath = path + "/reports/"
#             file_name = filepath + report.nodeid.replace("::", "_") + ".png"
#             if file_name:
#                 html = (
#                         '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" '
#                         'onclick="window.open(this.src)" align="right"/></div>' % file_name
#                 )
#                 extra.append(pytest_html.extras.html(html))
#         report.extra = extra