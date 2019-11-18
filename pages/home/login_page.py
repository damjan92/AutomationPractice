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

    logout_link = "//a[@class='logout']"
    success_signout = "//h3[contains(text(),'Create an account')]"

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
        self.driver.execute_script("window.scrollBy(0, 300);")
        self.clear_fields()
        self.enter_email(email)
        time.sleep(1)
        self.enter_password(password)
        self.click_button()

    def click_signOut(self):
        self.elementClick(self.logout_link, locatorType="xpath")

    def logout(self):
        self.click_signOut()


    def success_login(self):
        result = self.isElementPresent(self.succcesLogin, locatorType="xpath")
        return  result

    def unsuccess_login(self):
        result = self.isElementPresent(self.unsuccessLogin, locatorType="xpath")
        return result

    def success_logout(self):
        result = self.isElementPresent(self.success_signout, locatorType="xpath")
        return result



