import time
import pytest
import variables as globalvar
# Base class will have fixture setup and this can be inherited in tests
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pageObjects.dashboardpage import DashboardPage
from pageObjects.loginpage import LoginPage
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.mark.usefixtures("setup")
class BaseClass:
    def Login(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        self.driver = webdriver.Chrome(chrome_options=chrome_options)
        self.driver = webdriver.Chrome(options=chrome_options)
        loginPage = LoginPage(self.driver)
        loginPage.getUserName().send_keys(globalvar.username)
        loginPage.getPassword().send_keys(globalvar.password)
        loginPage.getrememberPassword().click()
        loginPage.getLoginButton().click()
        self.wait()

    def Dashboard(self, driver):
        dashboardPage = DashboardPage(self.driver)
        dashboardPage.getActiveUsers()
        element = WebDriverWait(driver, 10).until(EC.presence_of_element_located(DashboardPage))
        element.text()
        #dashboardPage.getDevicesStates().click()
        # dashboardPage.getDeviceCheckIns().click()
        # dashboardPage.getDeviceMakers().click()
        self.wait()

    def ProfileMenuIcon(self, driver):
        profilePage = ProfilePage(self.driver)
        profilePage.getProfileMenuIcon().click()
        profilePage.getName().click()
        profilePage.getLogout().click()
        self.wait()
        self.driver.quit()
        self.driver.close()

    # def logout(self):
    #     profilePage = ProfilePage(self.driver)
    #     profilePage.getMenuButton().click()
    #     profilePage.getLogOutButton().click()

    # def disableCookies(self):
    #     cookies = LoginPage(self.driver)
    #     try:
    #         if cookies.getDismissCookies().is_displayed():
    #             cookies.getDismissCookies().click()
    #             WeGuard.logger.debug("Cookies button is displayed")
    #     except NoSuchElementException:
    #         WeGuard.logger.debug("Cookies button is not displayed")
    #     self.wait()

    def wait(self):
        wait = time.sleep(10)

    # def every_downloads_chrome(self):
    #     if not self.driver.current_url.startswith("chrome://downloads"):
    #         self.driver.get("chrome://downloads/")
    #     return self.driver.execute_script("""
    #         var items = document.querySelector('downloads-manager')
    #             .shadowRoot.getElementById('downloadsList').items;
    #         if (items.every(e => e.state === "COMPLETE"))
    #             return items.map(e => e.fileUrl || e.file_url);
    #         """)

    def verifyByLinkText(self, text):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(By.LINK_TEXT, text))

    def verifyByXpath(self, xpath):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(By.XPATH, xpath))

    def verifyByClassName(self, className):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(By.CLASS_NAME, className))

    def verifyByCss(self, css):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(By.CSS_SELECTOR, css))

    def verifyById(self, id):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(By.ID, id))

    def verifyByName(self, name):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(By.NAME, name))

    def verifyByTagName(self, tagName):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(By.TAG_NAME, tagName))

    def verifyByLinkText(self, linkText):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(By.LINK_TEXT, linkText))

    def verifyByPartialText(self, partialText):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(By.PARTIAL_LINK_TEXT, partialText))

    def selectDropDown(self, locator, visibleText):
        dropdown = Select(locator)
        dropdown.select_by_visible_text(visibleText)

    def scrollDown(self):
        self.driver.execute_script("return document.body.scrollHeight")

    def scrollUp(self, element):
        self.driver.execute_script("return arguments[0].scrollIntoView(true);", element)
        self.wait()

    def backOption(self):
        self.driver.back()
        self.wait()