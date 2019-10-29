from pages.home.hover_page import HoverPage
from utilities.test_status import TestStatus
import unittest
import pytest

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class Hovertest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.hp = HoverPage(self.driver)
        self.ts = TestStatus(self.driver)

    @pytest.mark.run(order=1)
    def test_hovering(self):
        self.hp.add_to_chart()
        result = self.hp.success_addToChart()
        self.ts.mark_final("Test Hovering ", result, " Test is successful")


# py.test -s -v tests\home\hover_test.py --browser firefox