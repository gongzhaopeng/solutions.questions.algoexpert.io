import SolutionI_SameBSTs_Hard as program
import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        array_one = [10, 15, 8, 12, 94, 81, 5, 2, 11]
        array_two = [10, 8, 5, 15, 2, 12, 11, 94, 81]
        self.assertEqual(program.sameBsts(array_one, array_two), True)
