import unittest
from SolutionIII_Subarray_Sort_Hard import subarraySort


class TestSubarraySort(unittest.TestCase):
    def test_case1(self):
        array = [4, 8, 7, 12, 11, 9, -1, 3, 9, 16, -15, 51, 7]
        expected_indices = [0, 12]

        self.assertEqual(expected_indices, subarraySort(array))


if __name__ == '__main__':
    unittest.main()
