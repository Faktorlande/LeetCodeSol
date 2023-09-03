from typing import *
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1) & set(nums2))


sol = Solution()
nums1 = [4,9,5]
nums2 = [9,4,9,8,4]
print(sol.intersection(nums1, nums2))