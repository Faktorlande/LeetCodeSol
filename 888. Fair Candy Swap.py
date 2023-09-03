from typing import *

class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        sum_b = sum(bobSizes)
        sum_a = sum(aliceSizes)
        setB = set(bobSizes)
        for x in aliceSizes:
            if (x + (sum_b - sum_a)/2) in setB:
                return [x, int(x + (sum_b - sum_a)/2)]



        # for i in range(len(aliceSizes)):
        #     for j in range(len(bobSizes)):
        #         if sum_a - aliceSizes[i] + bobSizes[j] == target:
        #
        #             return list((aliceSizes[i], bobSizes[j])), serv_lst



sol = Solution()
aliceSizes = [1, 4]
bobSizes = [8, 5]

print(sol.fairCandySwap(aliceSizes, bobSizes))
#[1, 4, 0, 1]