import unittest


def threeNumberSum(array, targetSum):
    array.sort()
    triplets = []
    for i in range(len(array) - 2):
        head = array[i]
        rest = targetSum - head
        second_index = i + 1
        third_index = len(array) - 1
        while second_index < third_index:
            tail_sum = array[second_index] + array[third_index]
            if tail_sum < rest:
                second_index += 1
            elif tail_sum > rest:
                third_index -= 1
            else:
                triplets.append([
                    head,
                    array[second_index],
                    array[third_index]
                ])
                second_index += 1
                third_index -= 1
    return triplets


class TestThreeNumberSum(unittest.TestCase):
    def test_case1(self):
        array = [12, 3, 1, 2, -6, 5, -8, 6]
        target_num = 0
        self.assertEqual(
            threeNumberSum(array, target_num),
            [
                [-8, 2, 6],
                [-8, 3, 5],
                [-6, 1, 5]
            ]
        )


if __name__ == '__main__':
    unittest.main()
