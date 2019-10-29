from selenium import webdriver
import  os
import traceback

class WebDriverFactory():

    def __init__(self, browser):

        self.browser = browser


    def getWebDriverInstantce(self):

        baseUrl = "http://automationpractice.com/index.php"
        if self.browser == "ieexplorer":
            pass
            #driver = webdriver.Ie()
        elif self.browser == "chrome":
            #setting chrome
            driverLocation = "C:\\Users\\damja\\Desktop\\Python\\AutomationPractice\\libs\\chromedriver.exe"
            os.environ["webdriver.chrome.driver"] = driverLocation
            driver = webdriver.Chrome(driverLocation)
        elif self.browser == "firefox":
            driver = webdriver.Firefox(executable_path="C:\\Users\\damja\\Desktop\\Python\\AutomationPractice\libs\\geckodriver.exe")
        else:
            driver = webdriver.Firefox(executable_path="C:\\Users\\damja\\Desktop\\Python\\AutomationPractice\libs\\geckodriver.exe")

        driver.implicitly_wait(3)
        driver.maximize_window()
        driver.get(baseUrl)
        return driver
