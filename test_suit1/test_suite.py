import unittest

import sys
sys.path.append("D:\\00_MASTER OF COMPUTER SCIENCE_MUM\\00_Projects\\12_Automation Testing_Basic\\test_suit1")

# STEP 1: import all classes
from package1.TC_LoginTest import LoginTest
from package1.TC_SignupTest import SignUpTest
from package2.TC_PaymentTest import PaymentTest
from package2.TC_PaymentReturns import PaymentReturnTest


# STEP 2: get all tests using TestLoader().loadTestsFromTestCase( <classes in here> )
loginTest = unittest.TestLoader().loadTestsFromTestCase(LoginTest)
signUpTest = unittest.TestLoader().loadTestsFromTestCase(SignUpTest)
paymentTest = unittest.TestLoader().loadTestsFromTestCase(PaymentTest)
paymentReturnTest = unittest.TestLoader().loadTestsFromTestCase(PaymentReturnTest)

# STEP 3: create test suite
sanityTestSuite = unittest.TestSuite(loginTest, signUpTest)     # put 2 tests into a test suite called "Sanity Test suite"

# STEP 4: run test suite
unittest.TextTestRunner().run(sanityTestSuite)