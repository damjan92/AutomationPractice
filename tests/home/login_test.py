from pages.home.login_page import LoginPage

import unittest
import pytest

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class Logintest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.lp = LoginPage(self.driver)

    @pytest.mark.run(order = 5)
    def test_valid_login(self):
        self.lp.login("tester@email.com", "abcabc")
        result = self.lp.success_login()

    @pytest.mark.run(order = 1)
    def test_invalid_password(self):
        self.lp.login("tester@email.com", "abc")
        result = self.lp.unsuccess_login()
        assert result == True

    @pytest.mark.run(order = 2)
    def test_invalid_email(self):
        self.lp.login("test@email.com", "abcabc")
        result = self.lp.unsuccess_login()
        assert result == True

    @pytest.mark.run(order = 3)
    def test_invalid_email_and_passwvd(self):
        self.lp.login("test@email.com", "abc")
        result = self.lp.unsuccess_login()
        assert result == True

    @pytest.mark.run(order = 4)
    def test_invalid_with_blan_fields(self):
        self.lp.login("", "")
        result = self.lp.unsuccess_login()
        assert result == True

# py.test -s -v tests\home\login_test.py --browser firefox

