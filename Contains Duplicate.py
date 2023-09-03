from typing import *
# class Solution:
#     def containsDuplicate(self, nums: List[int]) -> bool:
#         if len(nums) > len(set(nums)):
#             return True
#         else:
#             return False
# nums = [1,2,3,1]
# print(Solution.containsDuplicate("", nums))


# class Solution:
#     def containsDuplicate(self, nums: List[int]) -> bool:
#         hash_table = {}
#         for i in range(len(nums)):
#             if hash_table.setdefault(nums[i]) is not None:
#                 return True
#             else:
#                 hash_table[nums[i]] = True
#         return False
# nums = [1,3,5,2,1]
# print(Solution.containsDuplicate("", nums))

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        set_check = set()
        for i in range(len(nums)):
            if nums[i] in set_check:
                return True
            else:
                set_check.add(nums[i])
        return False
nums = [1,3,5,2,1]
print(Solution.containsDuplicate("", nums))
#Это решение превышает лимит по времени