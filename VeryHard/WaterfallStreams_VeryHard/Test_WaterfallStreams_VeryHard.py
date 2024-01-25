import unittest
from SolutionI_WaterfallStreams_VeryHard import waterfallStreams


class TestWaterfallStreams(unittest.TestCase):
    def test_case1(self):
        array = [
            [0, 0, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 0, 0],
            [0, 0, 1, 1, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [1, 1, 1, 0, 0, 1, 0],
            [0, 0, 0, 0, 0, 0, 1],
            [0, 0, 0, 0, 0, 0, 0],
        ]
        source = 3
        expected = [0, 0, 0, 25, 25, 0, 0]
        self.assertEqual(expected, waterfallStreams(array, source))


if __name__ == '__main__':
    unittest.main()
