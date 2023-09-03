from typing import *

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        uniq_elem_lst = 1
        for i in range(len(nums)-1):
            if nums[i] != nums[i+1]:
                uniq_elem_lst += 1


        if uniq_elem_lst <= 2:
            max_elem = nums[0]
            for num in nums:
                if num > max_elem:
                    max_elem = num
            return max_elem


        else:
            nums.sort()
            indx = len(nums)-3

            i = len(nums)-1
            while i >= indx:
                if nums[i] == nums[i-1]:
                    i -= 1
                    indx -= 1
                else:
                    i -= 1
            return nums[indx]

nums = [1,5,2,3]

sol = Solution()
print(sol.thirdMax(nums))