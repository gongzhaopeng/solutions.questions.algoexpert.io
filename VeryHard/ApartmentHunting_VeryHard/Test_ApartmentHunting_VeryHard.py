import json
import unittest
from SolutionII_ApartmentHunting_VeryHard import apartmentHunting


class TestApartmentHunting(unittest.TestCase):
    def test_case1(self):
        blocks = json.loads("""[
            {
                "gym": false,
                "school": true,
                "store": false
            },
            {
                "gym": true,
                "school": false,
                "store": false
            },
            {
                "gym": true,
                "school": true,
                "store": false
            },
            {
                "gym": false,
                "school": true,
                "store": false
            },
            {
                "gym": false,
                "school": true,
                "store": true
            }
        ]""")
        reqs = ["gym", "school", "store"]
        expected_index = 3

        self.assertEqual(expected_index, apartmentHunting(blocks, reqs))


if __name__ == '__main__':
    unittest.main()
