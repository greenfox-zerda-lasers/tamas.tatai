import unittest
from exc01 import divide_ten

class TestExc01(unittest.TestCase):

    def test_divide(self):
        self.assertEqual(divide_ten(0), 'fail!')

if __name__ == '__main__':
    unittest.main()
