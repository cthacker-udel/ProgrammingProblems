class Solution:
    memo = {}
    base = {0: 0, 1: 1, 2: 1}

    def tribonacci(self, n: int) -> int:
        if n < 3:
            return Solution.base[n]
        elif n in Solution.memo:
            return Solution.memo[n]
        else:
            return Solution.tribonacci(self, n - 1) + Solution.tribonacci(self, n - 2) + Solution.tribonacci(self, n - 3)


if __name__ == '__main__':
    sol = Solution()
    print(sol.tribonacci(4))
