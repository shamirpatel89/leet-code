class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        lowest = 1
        for num in nums:
            if num < lowest:
                continue
            elif num == lowest:
                lowest += 1
            else:
                return lowest

        return lowest
