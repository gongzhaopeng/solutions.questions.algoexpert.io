import unittest
from SolutionII_FourNumberSum_Hard import fourNumberSum


class TestFourNumberSum(unittest.TestCase):
    def test_case1(self):
        array = [7, 6, 4, -1, 1, 2]
        target_num = 16
        expected_quadruplets = [
            [7, 6, 4, -1],
            [7, 6, 1, 2]
        ]
        for q in expected_quadruplets:
            q.sort()

        actual_quadruplets = fourNumberSum(array, target_num)
        for q in actual_quadruplets:
            q.sort()

        self.assertCountEqual(actual_quadruplets, expected_quadruplets)


if __name__ == '__main__':
    unittest.main()
