
import time
from typing import List

memo = {}

def modifiedRodCut(n: int, prices: List[int], costs: List[int], ind = 0) -> int:
    """
    Modified rod cut algorithm

    Args:
        n (int): The rod length
        costs (List[int]): The array of costs

    Returns:
        int: The maximum revenue from cutting rod of length n
    """
    if ind == n:
        memo[ind] = prices[n]
        return prices[n]
    return max(prices[ind] - costs[ind], modifiedRodCut(n - (ind + 1), prices, costs, ind + 1))


max_price_memo = {}
def max_rod_price(n_len: int, prices: List[int]) -> int:
    max_price = prices[n_len]
    if n_len in max_price_memo:
        return max_price_memo[n_len]
    if n_len <= 1:
        max_price_memo[n_len] = prices[n_len]
        return prices[n_len]
    for i in range(1, n_len):
        max_price = max(max_price, max_rod_price(i, prices) + max_rod_price(n_len - i, prices))
    max_price_memo[n_len] = max_price
    return max_price

def text_cut_rod(n, text_prices):
    if n == 0:
        return 0
    q = float('-inf')
    for i in range(1, n + 1):
        q = max(q, text_prices[i] + text_cut_rod(n - i, text_prices))
    return q

### Problem 1
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
### Problem 1


if __name__ == '__main__':
    PRICES = [1, 2, 4, 5, 6, 4, 7, 2, 5, 5]
    print(max_rod_price_cost(9, PRICES, 2))



