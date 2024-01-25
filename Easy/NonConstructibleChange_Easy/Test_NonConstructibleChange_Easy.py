import unittest
from SolutionI_NonConstructibleChange_Easy import nonConstructibleChange


class TestTournamentWinner(unittest.TestCase):
    def test_case1(self):
        coins = [5, 7, 1, 1, 2, 3, 22]
        expected = 20
        self.assertEqual(expected, nonConstructibleChange(coins))


if __name__ == '__main__':
    unittest.main()
