from pages.home.hover_page import HoverPage
import unittest
import pytest

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class Hovertest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.hp = HoverPage(self.driver)

    @pytest.mark.run(order=1)
    def test_hovering(self):
        self.hp.add_to_chart()
        result = self.hp.success_addToChart()
        assert result == True

# py.test -s -v tests\home\hover_test.py --browser firefox