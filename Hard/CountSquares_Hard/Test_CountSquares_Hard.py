import unittest
from SolutionI_CountSquares_Hard import countSquares


class TestCountSquares(unittest.TestCase):
    def test_case1(self):
        points = [[1, 1], [0, 0], [0, 1], [1, 0]]
        expected = 1
        self.assertEqual(expected, countSquares(points))


if __name__ == '__main__':
    unittest.main()
