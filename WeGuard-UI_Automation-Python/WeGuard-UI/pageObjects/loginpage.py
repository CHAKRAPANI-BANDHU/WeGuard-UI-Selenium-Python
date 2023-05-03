from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    # Locators are declared for login page
    username = (By.XPATH,"//*[@formcontrolname='userName']")
    password = (By.XPATH,"//*[@formcontrolname='password']")

    # Remember Password
    rememberPassword = (By.XPATH, "//mat-slide-toggle[@id='mat-slide-toggle-1']/label/div")

    # Login Button
    loginButton = (By.XPATH,"//*[@id=\"mat-tab-content-0-0\"]/div/div/div/form/button")

    # Toast message
    AlertMessage = (By.XPATH,"//span[contains(.,'Successfully Logged In')]")

    # Every locator has one function defined to user in test class
    def getUserName(self):
        return self.driver.find_element(*LoginPage.username)

    def getPassword(self):
        return self.driver.find_element(*LoginPage.password)

    def getrememberPassword(self):
        return self.driver.find_element(*LoginPage.rememberPassword)

    def getLoginButton(self):
        return self.driver.find_element(*LoginPage.loginButton)

    def getAlertMessage(self):
        return self.driver.find_element(*LoginPage.AlertMessage)
