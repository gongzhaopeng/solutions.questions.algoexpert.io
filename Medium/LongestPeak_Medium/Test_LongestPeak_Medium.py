import unittest
from SolutionI_LongestPeak_Medium import longestPeak


class TestLongestPeak(unittest.TestCase):
    def test_case1(self):
        array = [1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3]
        expected = 6
        self.assertEqual(expected, longestPeak(array))

    def test_case2(self):
        array = [1, 3, 2]
        expected = 3
        self.assertEqual(expected, longestPeak(array))

    def test_case3(self):
        array = [5, 4, 3, 2, 1, 2, 1]
        expected = 3
        self.assertEqual(expected, longestPeak(array))

    def test_case4(self):
        array = [1, 2, 3, 3, 2, 1]
        expected = 0
        self.assertEqual(expected, longestPeak(array))


if __name__ == '__main__':
    unittest.main()
