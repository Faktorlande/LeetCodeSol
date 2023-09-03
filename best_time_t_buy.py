from typing import *
prices = list(range(1, 101))
# class Solution:
#     def maxProfit(self, prices: List[int])-> int:
#         max_profit = 0
#         iter = 0
#         for j in range(len(prices)):
#             for i in range(j, len(prices)-1):
#                 if prices[j] < prices[i+1] and prices[i+1] - prices[j]>max_profit:
#                     max_profit = prices[i+1] - prices[j]
#                 iter+=1
#
#         return max_profit, iter
#
#
# print(Solution.maxProfit('', prices))

class Solution:
    def maxProfit(self, prices: List[int])-> int:
        min_price = float('inf')
        max_profit = 0
        for i in range(len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]
            elif prices[i] - min_price > max_profit:
                max_profit = prices[i] - min_price
        return max_profit

print(Solution.maxProfit('', prices))