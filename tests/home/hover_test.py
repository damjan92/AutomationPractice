from pages.home.hover_page import HoverPage
from utilities.test_status import Status
import unittest
import pytest

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class Hovertest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.hp = HoverPage(self.driver)
        self.ts = Status(self.driver)

    @pytest.mark.run(order=1)
    def test_hovering(self):
        self.hp.add_to_chart()
        result = self.hp.success_addToChart()
        self.ts.mark_final("Test Hovering ", result, " Test is successful")


# Run tests
# py.test -s -v tests\home\login_test.py --browser firefox  / chrome