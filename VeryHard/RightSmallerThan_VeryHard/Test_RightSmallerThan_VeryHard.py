import unittest
from SolutionIII_RightSmallerThan_VeryHard import rightSmallerThan


class TestRightSmallerThan(unittest.TestCase):
    def test_case1(self):
        array = [8, 5, 11, -1, 3, 4, 2]
        expected = [5, 4, 4, 0, 1, 1, 0]
        self.assertEqual(expected, rightSmallerThan(array))


if __name__ == '__main__':
    unittest.main()
