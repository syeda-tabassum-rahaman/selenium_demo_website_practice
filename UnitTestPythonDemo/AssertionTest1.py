import unittest
from selenium import webdriver


class Test(unittest.TestCase):
    def testName(self):
        driver = webdriver.Chrome(executable_path="C:\drivers\chromedriver.exe")
        driver.get("https://www.google.com/")
        titleofWebPage = driver.title
        # asserted
        # self.assertEqual("Google", titleofWebPage, "webpage title is not same")
        self.assertNotEqual("Google111", titleofWebPage, "webpage title is not same")


if __name__ == "__main__":
    unittest.main()
