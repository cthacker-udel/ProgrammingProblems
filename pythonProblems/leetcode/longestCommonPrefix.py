from sys import prefix
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) > 0:
            strs = sorted(strs, key=len)
            base_word = strs[0]
            if base_word == '':
                return ''
            _ind = 0
            min_len = len(strs[0])
            valid_prefix = True
            prefix = ''
            while _ind <= min_len:
                for i in range(len(strs)):
                    if not strs[i].startswith(prefix):
                        valid_prefix = False
                        break
                if not valid_prefix:
                    return prefix[:-1]
                else:
                    prefix += base_word[_ind] if _ind != min_len else ''
                    _ind += 1
            return prefix
        return ''


if __name__ == '__main__':
    arr = ["a", "b"]
    sol = Solution()
    print(sol.longestCommonPrefix(arr))
