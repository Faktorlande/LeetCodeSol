from typing import *

class Solution:

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mediana_indc = len(nums)//2
        while mediana_indc != 1:
            if target > all(nums[mediana_indc:]):
                mediana_indc = len(nums[:mediana_indc]) // 2
            else:
                mediana_indc = len(nums[mediana_indc:]) // 2
            print('it')

        return f"значение {nums[mediana_indc]}, индекc {mediana_indc}"



print(Solution.twoSum('', [2,7,11,15], 3))
