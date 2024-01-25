import unittest
from SolutionIII_KnightConnection_Hard import knightConnection


class TestKnightConnection(unittest.TestCase):
    def test_case1(self):
        knight_a = [10, 10]
        knight_b = [-10, -10]
        expected = 7
        self.assertEqual(expected, knightConnection(knight_a, knight_b))


if __name__ == '__main__':
    unittest.main()
