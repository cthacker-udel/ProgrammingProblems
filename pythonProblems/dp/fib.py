class Solution:
    memo = {}

    def fib(self, n: int) -> int:
        if n in Solution.memo:
            return Solution.memo[n]
        elif n == 1 or n == 0:
            return n
        else:
            result = Solution.fib(self, n - 2) + Solution.fib(self, n - 1)
            Solution.memo[n] = result
            return result


if __name__ == '__main__':
    sol = Solution()
    sol.fib(2)
