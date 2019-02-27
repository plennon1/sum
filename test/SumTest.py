import unittest
from Sum import Sum

class MyTestCase(unittest.TestCase):
    def test_something(self):
        mySum = Sum()
        mySum.myprint()
        self.assertEqual(True, True)
#comment
    def test_something2(self):
        self.assertEqual(True, True)
if __name__ == '__main__':
    unittest.main()
