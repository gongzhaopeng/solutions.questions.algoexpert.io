import unittest
from SolutionI_LargestSubarrayWithSum_Hard import longestSubarrayWithSum


class TestLargestSubarrayWithSum(unittest.TestCase):
    def test_case1(self):
        array = [1, 2, 3, 4, 3, 3, 1, 2, 1]
        target_sum = 10
        expected = [4, 8]
        self.assertEqual(expected, longestSubarrayWithSum(array, target_sum))

    def test_case2(self):
        array = [0]
        target_sum = 0
        expected = [0, 0]
        self.assertEqual(expected, longestSubarrayWithSum(array, target_sum))


if __name__ == '__main__':
    unittest.main()
