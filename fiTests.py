import unittest
from fib import printer

class TestFib(unittest.TestCase):
    def setUp(self):
        pass
    def testAnswer(self):
        self.assertEqual(printer(3), [0, 1, 2], "failure")

    def testString(self):
        self.assertEqual(printer("a"), "please input integer", "failure")

if __name__ == "__main__":
    unittest.main()
