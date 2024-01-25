import unittest
from SolutionII_SmallestDifference_Medium import smallestDifference


class TestSmallestDifference(unittest.TestCase):
    def test_case1(self):
        array_one = [-1, 5, 10, 20, 3]
        array_two = [26, 134, 135, 15, 17]
        expected_pair = [20, 17]

        self.assertEqual(expected_pair, smallestDifference(array_one, array_two))


if __name__ == '__main__':
    unittest.main()
