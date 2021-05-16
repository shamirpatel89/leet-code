class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        index = 0
        previous_num = None
        while index < len(nums):
            current_num = nums[index]
            if current_num != previous_num:
                previous_num = current_num
                index += 1
            else:
                nums.pop(index)

        return len(nums)
