from typing import *

class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        sum_b = sum(bobSizes)
        sum_a = sum(aliceSizes)
        target =int((sum_a + sum_b)/2)


        for i in range(len(aliceSizes)):
            for j in range(len(bobSizes)):
                if sum_a - aliceSizes[i] + bobSizes[j] == target:

                    return list((aliceSizes[i], bobSizes[j]))





sol = Solution()
aliceSizes = [2]
bobSizes = [1,3]

print(sol.fairCandySwap(aliceSizes, bobSizes))