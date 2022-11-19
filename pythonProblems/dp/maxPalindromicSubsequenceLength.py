from pprint import pprint

dp = {}


def maxPalindromicSubsequenceLength(astr: str) -> int:
    if len(astr) <= 1:
        return len(astr)
    if astr in dp:
        return dp[astr]
    if astr[0] != astr[-1]:
        result = max(maxPalindromicSubsequenceLength(
            astr[:-1]), maxPalindromicSubsequenceLength(astr[1:]))
        dp[astr] = result
        return result
    result = 2 + maxPalindromicSubsequenceLength(astr[1:len(astr) - 1])
    dp[astr] = result
    return result


if __name__ == '__main__':
    astr = 'ABBDCACB'
    print(maxPalindromicSubsequenceLength(astr))
