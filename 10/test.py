import unittest
from .solution import count_in_list, get_and_remove_from_dict, remove_smallest_value, Dictionary


class MyTests(unittest.TestCase):
    def test_count_in_list(self):
        self.assertEqual(count_in_list([1, 2, 1, 2, 3, 5, 8, 4, 5, 1, 2, 43, 5], 1), 3)

    def test_get_and_remove_from_dict(self):
        d, v = get_and_remove_from_dict(
            {'a': 'animal', 'b': 'bob', 'c': 'curry'},
            'b',
        )
        self.assertEqual(d, {'a': 'animal', 'c': 'curry'})
        self.assertEqual(v, 'bob')

    def test_remove_smallest_value(self):
        self.assertEqual(remove_smallest_value([5, 3, 5, 6, 7, 4, 34, -17, -3, 0]), [5, 3, 5, 6, 7, 4, 34, -3, 0])

    def test_dictionary(self):
        d = Dictionary(
            pages=[
                {
                    'apple': 'A green fruit',
                    'anaconda': 'A scary snake',
                    'avocado': 'A disgusting piece of crap',
                 },
                {
                    'blind': 'Unable to see',
                    'bubba': 'The most amazing person',
                    'barn': 'A building found on a farm',
                }
            ],
            glossary={
                'apple': 0,
                'anaconda': 0,
                'avocado': 0,
                'blind': 1,
                'bubba': 1,
                'barn': 1,
            }
        )
        self.assertEqual(d.lookup_definition('bubba'), 'The most amazing person')


if __name__ == '__main__':
    unittest.main()
