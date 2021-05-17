from json import loads
from unittest import TestCase
from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []

        nums.sort()
        results = set()

        for i, x in enumerate(nums):
            j = i + 1
            k = len(nums) - 1
            target = 0 - x

            while j < k:
                sum = nums[j] + nums[k]
                if sum == target:
                    results.add((x, nums[j], nums[k]))
                    j += 1
                elif sum < target:
                    j += 1
                else:
                    k -= 1

        return results

class MyTest(TestCase):

    def test_(self):
        solution = Solution()
        with open('test.json') as test_json:
            test_case = loads(test_json.read())
            self.assertEqual(
                [],
                solution.threeSum(test_case)
            )

solution = Solution()
with open('test.json') as test_json:
    test_case = loads(test_json.read())
    print(solution.threeSum(test_case))
