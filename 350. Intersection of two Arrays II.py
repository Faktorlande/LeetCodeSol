from typing import *

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:

        sort_nums1 = sorted(nums1)
        sort_nums2 = sorted(nums2)
        i = 0
        j = 0
        result = []
        while i < len(sort_nums1) and j < len(sort_nums2):
            if sort_nums1[i] < sort_nums2[j]:
                i += 1
            elif sort_nums1[i] > sort_nums2[j]:
                j += 1

            else:
                result.append(sort_nums1[i])
                i += 1
                j += 1
        return result

sol = Solution()
nums1 = [4,9,5]
nums2 = [9,4,9,8,4]
print(sol.intersect(nums1, nums2))