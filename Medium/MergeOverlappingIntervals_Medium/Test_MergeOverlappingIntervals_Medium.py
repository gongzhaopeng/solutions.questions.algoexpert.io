import SolutionI_MergeOverlappingIntervals_Medium as program
import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        intervals = [[1, 2], [3, 5], [4, 7], [6, 8], [9, 10]]
        expected = [[1, 2], [3, 8], [9, 10]]
        actual = program.mergeOverlappingIntervals(intervals)
        self.assertEqual(expected, actual)
