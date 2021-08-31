import unittest

class Apptesting(unittest.TestCase):

    @unittest.SkipTest
    def test_search(self):
        print("This is search test")

    @unittest.skip("I am skipping this test")
    def test_advancedsearch(self):
        print("this is an advanced search method")

    @unittest.skipIf(1==1, "one is equal to one")
    def test_prepaidrecharge(self):
        print("this is pre-paid recharch")

    def test_loginbygmail(self):
        print("this is login by email")

    def test_loginbytwitter(self):
        print("this is loging by tweitter")

if __name__ == "__main__":
    unittest.main()