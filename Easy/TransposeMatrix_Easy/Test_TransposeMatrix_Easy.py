import unittest
from SolutionI_TransposeMatrix_Easy import transposeMatrix


class TestTournamentWinner(unittest.TestCase):
    def test_case1(self):
        matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        expected = [[1, 4, 7], [2, 5, 8], [3, 6, 9]]

        self.assertEqual(expected, transposeMatrix(matrix))


if __name__ == '__main__':
    unittest.main()
