import unittest
from exc03 import Person

class TestExc03(unittest.TestCase):
    def bad_birth(self):
        self.assertRaises(ValueError, 'Firpo', 2017)

if __name__ == '__main__':
    unittest.main()
