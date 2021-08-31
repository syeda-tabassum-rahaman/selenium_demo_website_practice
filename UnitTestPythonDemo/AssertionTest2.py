import unittest
from selenium import webdriver


class Test(unittest.TestCase):
    def testName(self):
        driver = webdriver.Chrome(executable_path="C:\drivers\chromedriver.exe")
        driver.get("https://www.google.com/")
        titleofWebPage = driver.title
        # asserted
        #self.assertTrue(titleofWebPage == "Google")
        self.assertFalse(titleofWebPage == "Google")


if __name__ == "__main__":
    unittest.main()
