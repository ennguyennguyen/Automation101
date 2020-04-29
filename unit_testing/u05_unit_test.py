# -- ASSERTTRUE / ASSERTFALSE
# -- AssertEqual is for 2 parameters, but if we have multiple parameters, we should use AssertTrue / AssertFalse

from selenium import webdriver
import unittest

class TestAsser(unittest.TestCase):
    def testAssertTrue(self):
        driver = webdriver.Chrome(executable_path = "C:\\chromedriver_win32\\chromedriver.exe")
        driver.get("https://www.google.com/")
        webTitle = driver.title

        # -- use assertTrue
        #self.assertTrue(webTitle == "Google")

        # -- use assertFalse
        self.assertFalse(webTitle != "Google")

if __name__ == "__main__":
    unittest.main()