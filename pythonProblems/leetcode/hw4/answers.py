from typing import List


## problem1
cost_memo = {}
def max_rod_price_cost(n_len: int, prices: List[int], cost: int) -> int:
    if n_len == 0:
        return 0
    if (n_len - 1) in cost_memo:
        return cost_memo[n_len - 1]
    max_cost = prices[n_len - 1] - cost
    for i in range(1, n_len):
        max_cost = max(max_cost, prices[n_len - 1], (prices[i] + max_rod_price_cost(n_len - i, prices, cost)) - cost)
    cost_memo[n_len] = max_cost
    return max_cost

## problem2
def lengthOfLIS(self, nums: List[int]) -> int:
    dp = [1] * len(nums)
    n = len(nums) - 1
    dp[n] = 1
    for i in range(len(nums) - 1, -1, -1):
        for j in range(i + 1, len(nums)):
            dp[i] = max(dp[i], 1 + dp[j] if nums[i] < nums[j] else 0)
    return max(dp)

