
from typing import List

### problem4
class Solution:
    def maxProfit(self, prices: List[int]):
        ## start at back, and compute greatest stock value on kth day
        min_amount = prices[0]
        max_profit = 0
        for i in range(len(prices) - 1):
            min_amount = min(min_amount, prices[i])
            max_profit = max(max_profit, prices[i] - min_amount)
        return max_profit


if __name__ == '__main__':
    prices = [7,1,5,3,6,4]
    sol = Solution()
    print(sol.maxProfit(prices))