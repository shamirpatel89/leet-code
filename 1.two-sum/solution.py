class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for first_index, first_num in enumerate(nums):
            for second_index in range(first_index + 1, len(nums)):
                second_num = nums[second_index]
                if first_index != second_index and first_num + second_num == target:
                    return [first_index, second_index]
