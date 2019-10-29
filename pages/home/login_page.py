from base.selenium_driver import SeleniumDriver
import utilities.custom_logger as cl
import time
import logging

class LoginPage(SeleniumDriver):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    #Locators

    sing_in = "//a[@class='login']"
    email_field = "email"
    password_field = "passwd"
    button_signin = "//p[@class='submit']//span[1]"

    succcesLogin = "//h1[@class='page-heading']"
    unsuccessLogin = "//p[contains(text(),'There is 1 error')]"

    def click_signIn(self):
        self.elementClick(self.sing_in, locatorType="xpath")

    def enter_email(self, email):
        self.sendKeys(email, self.email_field, locatorType="id")

    def enter_password(self, password):
        self.sendKeys(password, self.password_field, locatorType="id")

    def click_button(self):
        self.elementClick(self.button_signin, locatorType="xpath")

    def clear_fields(self):
        emailF = self.getElement(locator= self.email_field)
        emailF.clear()
        passwordF = self.getElement(locator= self.password_field)
        passwordF.clear()

    def login(self, email = "", password = ""):
        self.click_signIn()
        time.sleep(1)
        self.clear_fields()
        self.enter_email(email)
        time.sleep(1)
        self.enter_password(password)
        time.sleep(1)
        self.click_button()


    def success_login(self):
        result = self.isElementPresent(self.succcesLogin, locatorType="xpath")
        return  result

    def unsuccess_login(self):
        result = self.isElementPresent(self.unsuccessLogin, locatorType="xpath")
        return result


