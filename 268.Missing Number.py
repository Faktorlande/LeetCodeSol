from typing import *
class Solution:

    def missingNumber(self, nums: List[int]) -> int:
        for num in range(len(nums)):
            if num not in nums:
                return num

sol = Solution()
nums = [9,6,4,2,3,5,7,0,1]

print(sol.missingNumber(nums))