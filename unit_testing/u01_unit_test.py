import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

class SearchEngineTest(unittest.TestCase):
    def test_searchGoogle(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("https://www.google.com/")
        print("title of page is: " + self.driver.title)
        self.driver.close()

    def test_searchBing(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("https://www.bing.com/")
        print("title of page is: " + self.driver.title)
        self.driver.close()

if __name__ == "__main__":
    unittest.main()









