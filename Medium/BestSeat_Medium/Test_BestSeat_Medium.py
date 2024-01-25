import SolutionII_BestSeat_Medium as program
import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        seats = [1, 0, 1, 0, 0, 0, 1]
        expected = 4
        actual = program.bestSeat(seats)
        self.assertEqual(actual, expected)
