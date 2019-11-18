from pages.home.login_page import LoginPage
from utilities.test_status import Status

import unittest
import pytest
from ddt import ddt, data, unpack
from utilities.read_data import getCSVdata


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
@ddt
class LoginTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.lp = LoginPage(self.driver)
        self.ts = Status(self.driver)

    @pytest.mark.run(order = 6)
    def test_logout(self):
        self.lp.logout()
        result = self.lp.success_logout()
        self.ts.mark_final("Test valid sign out", result, "Sign out is successful")

    @pytest.mark.run(order = 5)
    def test_valid_login(self):
        self.lp.login("tester@email.com", "abcabc")
        result = self.lp.success_login()
        self.ts.mark_final("Test valid Login", result, "Login was successful")

    @pytest.mark.run(order = 1)
    @data(*getCSVdata("C:\\Users\\damja\\Desktop\\Python\\AutomationPractice\\test_data.csv"))
    @unpack
    def test_invalid_login(self, email, password):
        self.lp.login(email, password)
        result = self.lp.unsuccess_login()
        self.ts.mark_final("Test invalid password", result, "Login was unsuccessful")

    # @pytest.mark.run(order = 2)
    # def test_invalid_email(self):
    #     self.lp.login("test@email.com", "abcabc")
    #     result = self.lp.unsuccess_login()
    #     self.ts.mark_final("Test invalid email", result, "Login was unsuccessful")
    #
    # @pytest.mark.run(order = 3)
    # def test_invalid_email_and_passwvd(self):
    #     self.lp.login("test@email.com", "abc")
    #     result = self.lp.unsuccess_login()
    #     self.ts.mark_final("Test invalid email and password", result, "Login was unsuccessful")
    #
    # @pytest.mark.run(order = 4)
    # def test_invalid_with_blan_fields(self):
    #     self.lp.login("", "")
    #     result = self.lp.unsuccess_login()
    #     self.ts.mark_final("Test invalid with blank fields", result, "Login was unsuccessful")


# Run tests
# py.test -s -v tests\home\login_test.py --browser firefox  / chrome

