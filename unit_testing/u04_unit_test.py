# -- ASSERTEQUAL & ASSERTNOTEQUAL
# -- Assertion is the check point (verificaton) for the test case to evaluate some items
# -- Helps in report generation, based on the assertion the test execution report will be generated

from selenium import webdriver
import unittest

class TestAsser(unittest.TestCase):
    def test_title(self):
        driver = webdriver.Chrome(executable_path = "C:\\chromedriver_win32\\chromedriver.exe")
        driver.get("https://www.google.com/")
        webTitle = driver.title

        # -- using AsserEqual
        #self.assertEqual("Google", webTitle)

        # -- using AssertNotEqual
        self.assertNotEqual("Google.com", webTitle)

if __name__ == "__main__":
    unittest.main()
