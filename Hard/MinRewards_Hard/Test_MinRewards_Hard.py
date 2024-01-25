import unittest
from SolutionII_MinRewards_Hard import minRewards


class TestMinRewards(unittest.TestCase):
    def test_case1(self):
        scores = [8, 4, 2, 1, 3, 6, 7, 9, 5]
        expected = 25

        self.assertEqual(expected, minRewards(scores))


if __name__ == '__main__':
    unittest.main()
