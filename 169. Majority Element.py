from typing import *
class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        hashe_map = {}
        for num in nums:
            hashe_map[num] = hashe_map.get(num, 0) + 1
        max_value = float('-inf')
        major_elem = 0
        for k, v in hashe_map.items():
            if v > max_value:
                max_value = v
                major_elem = k

        return major_elem




nums = [3,2,3]
sol = Solution()
print(sol.majorityElement(nums))