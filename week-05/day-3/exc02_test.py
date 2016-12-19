import unittest
from exc02 import line_number

class TestExc02(unittest.TestCase):
    def test_no_txt(self):
        self.assertEqual(line_number('lofasz.txt'), 0)

if __name__ == '__main__':
    unittest.main()
