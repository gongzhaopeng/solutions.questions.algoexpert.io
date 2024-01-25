import unittest
from SolutionII_MinimumAreaRectangle_VeryHard import minimumAreaRectangle


class TestMinimumAreaRectangle(unittest.TestCase):
    def test_case1(self):
        points = [
            [0, 1],
            [0, 0],
            [2, 1],
            [2, 0],
            [4, 0],
            [4, 1],
            [0, 2],
            [2, 2],
            [4, 2],
            [6, 0],
            [6, 1],
            [6, 2],
            [7, 1],
            [7, 0]
        ]
        expected = 1
        self.assertEqual(expected, minimumAreaRectangle(points))


if __name__ == '__main__':
    unittest.main()
