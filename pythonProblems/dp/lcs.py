from pprint import pprint
from typing import List

def find_subsequence_len(str1: str, str2: str, max_length = 0) -> int:
    for ind, elem in enumerate(str1):
        if elem in str2:
            max_length = max(max_length, 1 + find_subsequence_len(str1[ind + 1:], str2[str2.index(elem) + 1:]))
    return max_length
    

def lcs(substr1: str, substr2: str) -> int:
    while len(substr1) > 0 and len(substr2) > 0:
        if substr1[-1] != substr2[-1]:
            return max(lcs(substr1[:-1], substr2), lcs(substr1, substr2[:-1]))
        return 1 + lcs(substr1[:-1], substr2[:-1])
    return 0


if __name__ == '__main__':
    x = 'abcbdab'
    y = 'bdcaba'
    print(lcs(x, y))


        