import unittest
from SolutionII_ArrayOfProducts_Medium import arrayOfProducts


class TestArrayOfProducts(unittest.TestCase):
    def test_case1(self):
        array = [5, 1, 4, 2]
        expected = [8, 40, 10, 20]
        self.assertEqual(expected, arrayOfProducts(array))


if __name__ == '__main__':
    unittest.main()
