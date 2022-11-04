from typing import List


class Solution:
    dp = []

    def minCostClimbingStairs(self, cost: List[int], ind=None) -> int:
        Solution.dp = [-1] * (len(cost) + 1)
        Solution.minCost(self, cost, len(cost))
        print(Solution.dp)
        return Solution.dp[-1]

    def minCost(self, cost: List[int], ind) -> int:
        if Solution.dp[ind] != -1:
            return Solution.dp[ind]
        elif ind <= 1:
            Solution.dp[ind] = cost[ind]
            return cost[ind]
        else:
            adding_cost = 0
            if ind != len(cost):
                adding_cost = cost[ind]
            result = adding_cost + min(Solution.minCost(
                self, cost, ind - 1), Solution.minCost(self, cost, ind - 2))
            Solution.dp[ind] = result
            return Solution.dp[ind]


if __name__ == '__main__':
    arr = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
    sol = Solution()
    print(sol.minCostClimbingStairs(arr))
