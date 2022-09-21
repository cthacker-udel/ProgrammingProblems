from turtle import right


class Solution:
    def longestPalindrome(self, s: str) -> str:
        hashed_str = '#'.join('^{}$'.format(s))
        n = len(hashed_str)
        lps = [0] * n
        center = right = 0
        for i in range(1, n - 1):
            lps[i] = (right > i) and min(right - i, lps[2 * center - i])

            while hashed_str[i + 1 + lps[i]] == hashed_str[i - 1 - lps[i]]:
                lps[i] += 1

            if i + lps[i] > right:
                center, right = i, i + lps[i]

        maxlen, centerIndex = max((n, i) for i, n in enumerate(lps))
        return s[(centerIndex - maxlen) // 2: (centerIndex + maxlen) // 2]


if __name__ == '__main__':
    sol = Solution()
    print(sol.longestPalindrome("cbbd"))
