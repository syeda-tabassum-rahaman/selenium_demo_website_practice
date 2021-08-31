import unittest

from selenium import webdriver

class Test(unittest.TestCase):
    def testName(self):
        driver1 = webdriver.Chrome(executable_path="C:\drivers\chromedriver.exe")

        #driver2 = None

        #self.assertIsNone(driver2)
        self.assertIsNotNone(driver1)



if __name__ == "__main__":
    unittest.main()

