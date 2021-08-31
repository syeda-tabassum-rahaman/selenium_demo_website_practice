import unittest

from Package1.TC_LoginTest import LoginTest
from Package1.TC_SignupTest import SignupTest

from Package2.TC_PaymentTest import PaymentTest
from Package2.TC_paymentReturnTest import PaymentReturnTest

# Get all tests from LoginTest, SignUpTest, PaymentTest and PaymentReturnTest

TC1 = unittest.TestLoader().loadTestsFromTestCase(LoginTest)
TC2 = unittest.TestLoader().loadTestsFromTestCase(SignupTest)
TC3 = unittest.TestLoader().loadTestsFromTestCase(PaymentTest)
TC4 = unittest.TestLoader().loadTestsFromTestCase(PaymentReturnTest)

# Creating test Suites

sanityTestSuite = unittest.TestSuite([TC1, TC2])
functionalTestSuite = unittest.TestSuite([TC3, TC4])
masterTestSuit = unittest.TestSuite([TC1, TC2, TC3, TC4])

unittest.TextTestRunner().run(masterTestSuit)

