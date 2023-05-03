from selenium.webdriver.common.by import By

class ProfilePage:
    def __init__(self, driver):
        self.driver = driver

    ActiveUsers = (By.XPATH, "//*[@id=\"drop-mini\"]/mat-sidenav-content/div[1]/ng-component/mat-card/div/div[1]/app-dashboard-header/div/div[1]/div[1]")
    ActiveDevices = (By.XPATH, "//div[contains(text(), 'Active Devices')]")

    # Every locator has one function defined to user in test class
    # def getDashboard(self):
    #     return self.driver.find_element(*DashboardPage.Dashboard)

    def getDevicesStates(self):
        return self.driver.find_element(*ProfilePage.DevicesStates)
