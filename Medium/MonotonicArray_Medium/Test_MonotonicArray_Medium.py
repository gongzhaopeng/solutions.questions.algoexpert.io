import unittest
from SolutionI_MonotonicArray_Medium import isMonotonic


class TestMoveElementToEnd(unittest.TestCase):
    def test_case1(self):
        array = [-1, -5, -10, -1100, -1100, -1101, -1102, -9001]
        expected = True
        self.assertEqual(expected, isMonotonic(array))


if __name__ == '__main__':
    unittest.main()
