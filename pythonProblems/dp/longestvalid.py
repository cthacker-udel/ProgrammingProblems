class Solution:
    def longestValidParentheses(self, s: str) -> int:
        dp = [0] * len(s)
        for i in range(len(s)):
            if s[i] == ')':
                if i - 1 < 0:
                    continue
                elif s[i - 1] == '(':
                    dp[i] = dp[i - 2] + 2
                elif i - dp[i - 1] - 1 < 0:
                    continue
                elif s[i - dp[i - 1] - 1] == '(':
                    ## matching over the current pair
                    dp[i] = dp[i - 1] + 2 + dp[i - dp[i - 1] - 2]
        return max(dp)


if __name__ == '__main__':
    sol = Solution()
    print(sol.longestValidParentheses("(()))())("
                                      ))
