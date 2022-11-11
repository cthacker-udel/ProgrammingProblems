from typing import List


def min_coins(n: int, coins: List[int]):
    """_summary_

    Args:
        n (int): _description_
        coins (List[int]): _description_
    """
    dp = [0] + ([float('inf')] * n)
    for i in range(n + 1):  # iterate through all the potential coin value targets 0...n
        # iterate through all potential coins in the list and apply it to the sub-problems,
        for j in range(len(coins)):
            # checking if the subproblem before it has less steps, then add one to the final result
            # checking if the current target - the coin we're on right now has been solved,
            if (i - coins[j]) < 0:
                # if it has not, then we continue
                continue
            # dp[i] represents the current potential target coin value
            # dp[i - coins[j]] represents the subproblem of the potential target coin value - the current coin
            # check the current target we're on, check if the current target has less steps
            dp[i] = min(dp[i], dp[i - coins[j]] + 1)
            # then the subproblem of the current target - the coin we're on currently (aka previous subproblem), then add one to that result
            # because we are evaluating a previous subproblem and in order to reach the current target we add one step to it.
    print(dp[n] if dp[n] != float('inf') else -1)


if __name__ == '__main__':
    first_line = input()
    target = int(first_line.split(" ")[1])
    arr_line = input()
    arr = [int(x) for x in arr_line.split(" ")]
    min_coins(target, arr)
