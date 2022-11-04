class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0, 1]
        for i in range(1, n + 1):
            dp.append(dp[i - 1] + dp[i - 2])
        print(dp)


if __name__ == '__main__':
    sol = Solution()
    print(sol.climbStairs(5))
