import unittest
from SolutionII_MoveElementToEnd_Medium import moveElementToEnd


class TestMoveElementToEnd(unittest.TestCase):
    def test_case1(self):
        array = [2, 1, 2, 2, 2, 3, 4, 2]
        to_move = 2

        expected = [4, 1, 3, 2, 2, 2, 2, 2]
        self.assertEqual(expected, moveElementToEnd(array, to_move))


if __name__ == '__main__':
    unittest.main()
