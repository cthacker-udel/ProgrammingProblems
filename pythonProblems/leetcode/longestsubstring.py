class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest_substring = []
        _max = 0
        for i in range(len(s)):
            _char = s[i]
            if _char in longest_substring:
                _ind = longest_substring.index(_char)
                del longest_substring[0:_ind + 1]
                longest_substring.append(_char)
                _max = max(_max, len(longest_substring))
            else:
                longest_substring.append(_char)
                _max = max(_max, len(longest_substring))
        return _max


if __name__ == '__main__':
    sol = Solution()
    print(sol.lengthOfLongestSubstring("abcabcbb"))
