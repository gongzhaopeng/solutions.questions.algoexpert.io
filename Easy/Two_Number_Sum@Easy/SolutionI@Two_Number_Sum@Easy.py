import unittest


def twoNumberSum(array, targetSum):
    array.sort()
    left_index = 0
    right_index = len(array) - 1
    while left_index < right_index:
        current_sum = array[left_index] + array[right_index]
        if current_sum == targetSum:
            return [array[left_index], array[right_index]]
        elif current_sum < targetSum:
            left_index += 1
        else:
            right_index -= 1
    return []


class TestTwoNumberSum(unittest.TestCase):
    def test_case1(self):
        array = [3, 5, -4, 8, 11, 1, -1, 6]
        target_num = 10
        self.assertCountEqual(
            twoNumberSum(array, target_num),
            [-1, 11]
        )


if __name__ == '__main__':
    unittest.main()
