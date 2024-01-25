import unittest
from SolutionII_LargestRange_Hard import largestRange


class TestLargestRange(unittest.TestCase):
    def test_case1(self):
        array = [1, 11, 3, 0, 15, 5, 2, 4, 10, 7, 12, 6]
        expected = [0, 7]

        self.assertEqual(expected, largestRange(array))


if __name__ == '__main__':
    unittest.main()
