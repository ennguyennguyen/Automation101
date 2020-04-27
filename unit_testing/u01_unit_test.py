import unittest
from selenium import webdriver

class SearchEngineTest(unittest.TestCase):
    def test_searchGoogle(self):
        self.driver = webdriver.Chrome(executable_path = "C:\\chromedriver_win32\\chromedriver.exe")
        self.driver.get("https://www.google.com/")
        print("title of page is: " + self.driver.title)
        self.driver.close()

    def test_searchBing(self):
        self.driver = webdriver.Chrome(executable_path = "C:\\chromedriver_win32\\chromedriver.exe")
        self.driver.get("https://www.bing.com/")
        print("title of page is: " + self.driver.title)
        self.driver.close()

if __name__ == "__main__":
    unittest.main()









