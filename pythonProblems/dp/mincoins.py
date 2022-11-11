from typing import List


def min_coins(n: int, coins: List[int]):
    dp = [0] * n
    for i in range(n):  # iterate through all the potential targets 0...n
        for j in range(len(coins)):
            dp[i] = min(dp[i], dp[i - j]) + 1
    return min(dp)


if __name__ == '__main__':
    coins = [1, 5, 7]
    target = 11
    print(min_coins(target, coins))
