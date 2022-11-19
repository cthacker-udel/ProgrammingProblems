from pprint import pprint
from typing import List


def find_subsequence_len(str1: str, str2: str, max_length=0) -> int:
    for ind, elem in enumerate(str1):
        if elem in str2:
            max_length = max(
                max_length, 1 + find_subsequence_len(str1[ind + 1:], str2[str2.index(elem) + 1:]))
    return max_length


def lcs(substr1: str, substr2: str) -> int:
    while len(substr1) > 0 and len(substr2) > 0:
        if substr1[-1] != substr2[-1]:
            return max(lcs(substr1[:-1], substr2), lcs(substr1, substr2[:-1]))
        return 1 + lcs(substr1[:-1], substr2[:-1])
    return 0


def print_lcs(substr1: str, substr2: str) -> str:
    table = []
    # initialize table
    for _ in substr1 + " ":
        table_row = []
        for __ in substr2 + " ":
            table_row.append(0)
        table.append(table_row)
        table_row = []

    for i in range(1, len(substr1) + 1):
        for j in range(1, len(substr2) + 1):
            if substr2[j - 1] == substr1[i - 1]:  # if both characters match
                # characters match, set the diagonal cell to the curr value + 1
                table[i][j] = table[i - 1][j - 1] + 1
            else:
                # either up or left in the lookup table
                table[i][j] = max(table[i - 1][j], table[i][j - 1])
    # start at bottom right, and follow the path, taking a diagonal left with the letters are the same

    startCol = len(table[len(table) - 1]) - 1
    startRow = len(table) - 1

    _substr1 = " " + substr1
    _substr2 = " " + substr2
    substr = ''
    pprint(table)
    while startCol != 0 and startRow != 0:
        if _substr1[startRow] == _substr2[startCol]:
            # jump diagonal, add letter
            substr += _substr1[startRow]
            startRow -= 1
            startCol -= 1
        else:
            # evaluate left
            left_ = -1
            if startCol > 0:
                left_ = table[startRow][startCol - 1]
            # evaluate top
            top_ = -1
            if startRow > 0:
                top_ = table[startRow - 1][startCol]

            if left_ == top_:
                startCol -= 1
            if left_ != -1 and top_ != -1:
                startRow -= 1 if top_ > left_ else 0
                startCol -= 1 if left_ > top_ else 0
            if left_ == -1:
                # move up
                startRow -= 1
            if top_ == -1:
                startCol -= 1
    return substr[::-1]


if __name__ == '__main__':
    x = 'abcbdab'
    y = 'bdcaba'
    print(lcs(x, y))
    x2 = 'xmjyauzadfsf'
    y2 = 'mzjawxuwqrwe'
    print(print_lcs(x2, y2))
