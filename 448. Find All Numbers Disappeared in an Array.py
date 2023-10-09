from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        hash_table = {}
        answer_lst = []

        for num in nums:
            if not hash_table.get(num):
                hash_table[num] = num
            else:
                continue
        for i in range(1, len(nums) + 1):
            if not hash_table.get(i):
                answer_lst.append(i)
        return answer_lst
