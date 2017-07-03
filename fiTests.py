import unittest
from fib import printer

class TestFib(unittest.TestCase):
    def setUp(self):
        pass
    def testAnswer(self):
        self.assertEqual(printer(3), [0, 1, 2], "failure")

    def testString(self):
        self.assertEqual(printer("a"), "please input integer", "failure")

    def testInvalidNumber(self):
        self.assertEqual(printer(0), "integer must be greater than 1", "failure")

    def testOne(self):
        self.assertEqual(printer(1), [0], "failure")

    def testOtherObjects(self):
        self.assertEqual(printer([1,2,3]), "please input integer", "failure")


if __name__ == "__main__":
    unittest.main()
