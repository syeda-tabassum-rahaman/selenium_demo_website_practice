import unittest
class Test(unittest.TestCase):
    def testName(self):
        list = {"python", "selenium", "Java"}

        #self.assertIn("python", list)
        self.assertNotIn("python", list)


if __name__ == "__main__":
    unittest.main()