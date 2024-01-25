import unittest
from SolutionI_LineThroughPoints_VeryHard import lineThroughPoints
from fractions import Fraction


class TestLineThroughPoints(unittest.TestCase):
    def test_case1(self):
        points = [[1, 1], [2, 2], [3, 3], [0, 4], [-2, 6], [4, 0], [2, 1]]
        expected = 4
        self.assertEqual(expected, lineThroughPoints(points))
        print(Fraction(100, 10).as_integer_ratio())


if __name__ == '__main__':
    unittest.main()
