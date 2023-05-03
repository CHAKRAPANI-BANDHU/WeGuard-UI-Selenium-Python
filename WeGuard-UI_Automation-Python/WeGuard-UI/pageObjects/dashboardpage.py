from selenium.webdriver.common.by import By

class DashboardPage:
    def __init__(self, driver):
        self.driver = driver

    # Locators are declared for Dashboard page
    # Dashboard = (By.XPATH, "//a[contains(@href, '#/dashboard')]")
    ActiveUsers= (By.XPATH, "//div[text()[normalize-space()='Active Users']]")
    ActiveUsersCount= (By.XPATH,"//*[@id='drop-mini']/mat-sidenav-content/div[1]/ng-component/mat-card/div/div[1]/app-dashboard-header/div/div[1]/div[1]/div[1]")
    ActiveDevices = (By.XPATH, "//div[text()[normalize-space()='Active Devices']]")
    ActiveDevicesCount= (By.XPATH,"//*[@id='drop-mini']/mat-sidenav-content/div[1]/ng-component/mat-card/div/div[1]/app-dashboard-header/div/div[1]/div[2]/div[1]")
    NonCompliant = (By.XPATH, "//div[normalize-space()='Non-Compliant']")
    NonCompliantCount=(By.XPATH,"//*[@id='drop-mini']/mat-sidenav-content/div[1]/ng-component/mat-card/div/div[1]/app-dashboard-header/div/div[1]/div[3]/div[1]")
    Files= (By.XPATH, "//div[normalize-space()='Files']")
    FilesCount=(By.XPATH,"//*[@id='drop-mini']/mat-sidenav-content/div[1]/ng-component/mat-card/div/div[1]/app-dashboard-header/div/div[2]/div[1]/div[1]")
    Messages= (By.XPATH, "//div[normalize-space()='Messages']")
    MessagesCount=(By.XPATH,"//*[@id='drop-mini']/mat-sidenav-content/div[1]/ng-component/mat-card/div/div[1]/app-dashboard-header/div/div[2]/div[2]/div[1]")
    Calls= (By.XPATH, "//div[normalize-space()='Calls']")
    CallsCount=(By.XPATH,"//*[@id='drop-mini']/mat-sidenav-content/div[1]/ng-component/mat-card/div/div[1]/app-dashboard-header/div/div[2]/div[3]/div[1]")
    DevicesStatus = (By.XPATH, "(//*[@class='chartjs-render-monitor'])[1]")
    DeviceCheckIns = (By.XPATH, "(//*[@class='chartjs-render-monitor'])[2]")
    DeviceMakers = (By.CSS_SELECTOR, "foreignobject")

    # Recent Activity Refresh Icon
    RefreshIconInRecentActivity = (By.XPATH, "//mat-icon[contains(.,'refresh')]")

    # High Data Consuming Devices Locators
    FirstDeviceID = (By.XPATH, "//mat-sidenav-container[@id='drop-mini']/mat-sidenav-content/div/ng-component/mat-card/div/div/div[2]/app-high-dataconsuming-devices-table/div[2]/mat-table/mat-row[1]/mat-cell[2]/section/u")
    SecondDeviceID = (By.XPATH, "//mat-sidenav-container[@id='drop-mini']/mat-sidenav-content/div/ng-component/mat-card/div/div/div[2]/app-high-dataconsuming-devices-table/div[2]/mat-table/mat-row[2]/mat-cell[2]/section/u")
    ThirdDeviceID = (By.XPATH, "//mat-sidenav-container[@id='drop-mini']/mat-sidenav-content/div/ng-component/mat-card/div/div/div[2]/app-high-dataconsuming-devices-table/div[2]/mat-table/mat-row[3]/mat-cell[2]/section/u")
    FourthDeviceID = (By.XPATH, "//mat-sidenav-container[@id='drop-mini']/mat-sidenav-content/div/ng-component/mat-card/div/div/div[2]/app-high-dataconsuming-devices-table/div[2]/mat-table/mat-row[4]/mat-cell[2]/section/u")
    FifthDeviceID = (By.XPATH, "//mat-sidenav-container[@id='drop-mini']/mat-sidenav-content/div/ng-component/mat-card/div/div/div[2]/app-high-dataconsuming-devices-table/div[2]/mat-table/mat-row[5]/mat-cell[2]/section/u")

    # Every locator has one function defined to user in test class
    # def getDashboard(self):
    #     return self.driver.find_element(*DashboardPage.Dashboard)

    def getDevicesStates(self):
        return self.driver.find_element(*DashboardPage.DevicesStatus)

    def getDeviceCheckIns(self):
        return self.driver.find_element(*DashboardPage.DeviceCheckIns)

    def getDeviceMakers(self):
        return self.driver.find_element(*DashboardPage.DeviceMakers)

    def getRefreshIconInRecentActivity(self):
        return self.driver.find_element(*DashboardPage.RefreshIconInRecentActivity)

    def getActiveUsers(self):
        return self.driver.find_element(*DashboardPage.ActiveUsers)

    def getActiveUsersCount(self):
        return self.driver.find_element(*DashboardPage.ActiveUsersCount)

    def getActiveDevices(self):
        return self.driver.find_element(*DashboardPage.ActiveDevices)

    def getActiveDevicesCount(self):
        return self.driver.find_element(*DashboardPage.ActiveDevicesCount)

    def getNonCompliant(self):
        return self.driver.find_element(*DashboardPage.NonCompliant)

    def getNonCompliantCount(self):
        return self.driver.find_element(*DashboardPage.NonCompliantCount)

    def getFiles(self):
        return self.driver.find_element(*DashboardPage.Files)

    def getFilesCount(self):
        return self.driver.find_element(*DashboardPage.FilesCount)

    def getMessages(self):
        return self.driver.find_element(*DashboardPage.Messages)

    def getMessagesCount(self):
        return self.driver.find_element(*DashboardPage.MessagesCount)

    def getCalls(self):
        return self.driver.find_element(*DashboardPage.Calls)

    def getCallsCount(self):
        return self.driver.find_element(*DashboardPage.CallsCount)

    def getFirstDeviceID(self):
        return self.driver.find_element(*DashboardPage.FirstDeviceID)

    def getSecondDeviceID(self):
        return self.driver.find_element(*DashboardPage.SecondDeviceID)

    def getThirdDeviceID(self):
        return self.driver.find_element(*DashboardPage.ThirdDeviceID)

    def getFourthDeviceID(self):
        return self.driver.find_element(*DashboardPage.FourthDeviceID)

    def getFifthDeviceID(self):
        return self.driver.find_element(*DashboardPage.FifthDeviceID)