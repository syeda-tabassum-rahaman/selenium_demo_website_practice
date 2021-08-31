import unittest

class PaymentTest(unittest.TestCase):

    def test_paymentindollor(self):
        print("This is payment in dollor test")
        self.assertTrue(True)

    def test_paymentinrupee(self):
        print("This is payment in rupee test")
        self.assertTrue(True)

if __name__ == "__main__":
    unittest.main()