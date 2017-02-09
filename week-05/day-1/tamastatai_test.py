from tamastatai_work import anagram, count_letters
import unittest

class TestWork(unittest.TestCase):
    def test_anagram_lowercase(self):
        self.assertTrue(anagram('lobab', 'Lobab'))

    def test_empty_anagram(self):
        self.assertTrue(anagram('', ''))

    def test_space_in_anagram(self):
        self.assertTrue(anagram('lobab', 'bab lo'))

    def test_with_numeric_numbers(self):
       self.assertRaises(AttributeError, anagram, 'bab', 1234)

    def test_count_letters(self):
        self.assertRaises(AttributeError, count_letters, 9756)

    def test_count_letters_whitespace(self):
        self.assertTrue(count_letters('das sadas da'))    

if __name__ == '__main__':
    unittest.main(exit = False)
