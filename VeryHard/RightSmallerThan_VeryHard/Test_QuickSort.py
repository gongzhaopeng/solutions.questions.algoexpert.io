import random
import unittest
from WRONG_SolutionI_RightSmallerThan_VeryHard import quick_sort


class TestQuickSort(unittest.TestCase):
    def test_case1(self):
        double = [1, 2]
        triple = [1, 2, 3]
        arrays = [
            [0],
            [1],
            *[[i, j] for j in double for i in double],
            *[[i, j, k] for k in triple for j in triple for i in triple],
        ]
        for i in range(100):
            to_shuffle = list(range(173))
            random.shuffle(to_shuffle)
            arrays.append(to_shuffle)
        for array in arrays:
            expected = sorted(array)
            quick_sort(array, 0, len(array))
            self.assertEqual(expected, array)


if __name__ == '__main__':
    unittest.main()
