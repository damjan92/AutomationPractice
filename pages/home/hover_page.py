from base.selenium_driver import SeleniumDriver
import utilities.custom_logger as cl
import time
import logging

class HoverPage(SeleniumDriver):

    log = cl.customLogger(logging.DEBUG)


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # locator add to chart

    hover_field = "/html[1]/body[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/ul[1]/li[1]/div[1]/div[1]/div[1]/a[1]/img[1]"
    add_to_btn = "/html[1]/body[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/ul[1]/li[1]/div[1]/div[2]/div[2]/a[1]/span[1]"
    proceedCheckout = "//span[contains(text(),'Proceed to checkout')]"


    def hover_action(self):
        self.mouse_hovering(self.hover_field, locatorType="xpath")

    def hover_click(self):
        self.elementClick(self.add_to_btn, locatorType="xpath")


    def success_addToChart(self):
        result = self.isElementPresent(self.proceedCheckout, locatorType="xpath")
        return result

    def add_to_chart(self):
        self.driver.execute_script("window.scrollBy(0, 600);")
        self.hover_action()
        self.hover_click()
        time.sleep(3)

