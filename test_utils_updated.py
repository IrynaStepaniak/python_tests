import unittest
import utils


class TestArrayUtils(unittest.TestCase):
    # import equals output

    def test_array_equals(self):
        n = [1, 2, 3]
        result = utils.reverse(n)
        self.assertEqual([1, 2, 3], result, "Arrays Not Equal")

    #None
    def test_array_none(self):
        n = NULL
        result = utils.reverse(n)
        self.assertIsNone(NULL, result, "Array is NULL")

    #[]
    def test_array_empty(self):
        n =[]
        result= utils.reverse(n)
        self.assertEqual([], result, "Empty Array")
