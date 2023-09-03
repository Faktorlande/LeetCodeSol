from typing import *
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_end = 0
        max_now = max(nums)
        if len(nums) == 1:
            return nums[0]
        for i in range(len(nums)):
            max_end += nums[i]
            if max_end < 0:
                max_end = 0
            elif max_now < max_end:
                max_now = max_end
        return max_now
nums = [-8, -2]
print(Solution.maxSubArray('', nums))