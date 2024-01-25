import unittest
from SolutionI_TournamentWinner_Easy import tournamentWinner


class TestTournamentWinner(unittest.TestCase):
    def test_case1(self):
        competitions = [
            ["HTML", "C#"],
            ["C#", "Python"],
            ["Python", "HTML"]
        ]
        results = [0, 0, 1]

        expected = "Python"
        self.assertEqual(expected, tournamentWinner(competitions, results))


if __name__ == '__main__':
    unittest.main()
