import unittest


def setUpModule():
    print("set up Module ")


def tearDownModule():
    print("tear down Module ")


class AppTesting(unittest.TestCase):
    @classmethod
    def setUp(self):
        print("This is login test")

    @classmethod
    def tearDown(self):
        print("this is logout test")

    @classmethod
    def setUpClass(cls):
        print("open application")

    @classmethod
    def tearDownClass(cls):
        print("close application")

    def test_search(self):
        print("this is a search test")

    def test_advancedsearch(self):
        print("this is an advance search test")

    def test_prepaidRecharge(self):
        print("this is a prepaid Recharge test")

    def test_postpaidRecharge(self):
        print("this is a post paidRecharge test")


if __name__ == "__main__":
    unittest.main()
