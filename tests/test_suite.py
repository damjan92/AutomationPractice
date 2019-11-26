import unittest
from tests.home.login_test import LoginTest
from tests.home.hover_test import Hovertest

tc1 = unittest.TestLoader().loadTestsFromTestCase(LoginTest)
tc2 = unittest.TestLoader().loadTestsFromTestCase(Hovertest)

testsuit = unittest.TestSuite([tc1, tc2])

unittest.TextTestRunner(verbosity=2).run(testsuit)

