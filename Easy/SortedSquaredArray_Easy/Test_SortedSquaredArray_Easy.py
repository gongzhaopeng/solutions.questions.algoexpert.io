import unittest
from SolutionI_SortedSquaredArray_Easy import sortedSquaredArray


class TestSortedSquaredArray(unittest.TestCase):
    def test_case1(self):
        array = [1, 2, 3, 5, 6, 8, 9]

        expected = [1, 4, 9, 25, 36, 64, 81]
        self.assertEqual(expected, sortedSquaredArray(array))


if __name__ == '__main__':
    unittest.main()
