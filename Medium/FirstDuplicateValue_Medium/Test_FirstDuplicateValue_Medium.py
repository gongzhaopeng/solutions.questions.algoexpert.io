import unittest
from SolutionI_FirstDuplicateValue_Medium import firstDuplicateValue


class TestFirstDuplicateValue(unittest.TestCase):
    def test_case1(self):
        array = [2, 1, 5, 2, 3, 3, 4]
        expected = 2
        self.assertEqual(expected, firstDuplicateValue(array))


if __name__ == '__main__':
    unittest.main()
