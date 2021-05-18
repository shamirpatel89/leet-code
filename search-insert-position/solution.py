from unittest import TestCase
from typing import List

class Solution:

    def _binary_search(self, nums, low, high, x) -> int:
        if low < high:
            mid = (high + low) // 2

            if x == nums[mid]:
                return mid
            elif x < nums[mid]:
                return self._binary_search(nums, low, mid - 1, x)
            else:
                return self._binary_search(nums, mid + 1, high, x)
        elif low == high:
            if x == nums[low]:
                return low
            elif x < nums[low]:
                return low
            else:
                return low + 1
        return low

    def searchInsert(self, nums: List[int], target: int) -> int:
        if target < nums[0]:
            return 0
        elif target > nums[-1]:
            return len(nums)

        return self._binary_search(nums, 0, len(nums) - 1, target)


class Test(TestCase):
    def test(self):
        solution  = Solution()
        for test_case in [
            [[1,3,5,6], 5, 2],
            [[1,3,5,6], 2, 1],
            [[1,3,5,6], 7, 4],
            [[1,3,5,6], 0, 0],
            [[1], 0, 0],
            [[1,3], 2, 1],
            [[1,2,3], 2, 1],
            [[1,2,3], 4, 3],
            [[1,3], 4, 2],
            [[3,5,7,9,10], 8, 3]
        ]:
            with self.subTest(test_case):
                self.assertEqual(
                    test_case[2],
                    solution.searchInsert(test_case[0], test_case[1])
                )
