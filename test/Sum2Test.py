import unittest
from Sum import Sum

class MyTestCase(unittest.TestCase):
    def test_something3(self):
        mySum = Sum()
        mySum.myprint()
        self.assertEqual(True, True)
#comment
    def test_something4(self):
        self.assertEqual(False, True)
if __name__ == '__main__':
    unittest.main()
