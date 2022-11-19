
from pprint import pprint


def longest_repeating_subsequence(astr: str) -> int:
    """
    Finds the longest repeating subsequence of a str

    Args:
        astr (str): The string to find the longest subsequence of

    Returns:
        int: the longest subsequence
    """
    table = []
    for _ in astr:
        table_row = []
        for __ in astr:
            table_row.append(0)
        table.append(table_row)
        table_row = []

    for i in range(len(astr)):
        for j in range(len(astr)):
            if i == 0 or j == 0:
                continue
            elif astr[i - 1] == astr[j - 1] and i != j:
                table[i][j] = table[i - 1][j - 1] + 1
            else:
                table[i][j] = max(table[i - 1][j], table[i][j - 1])
    return max(max(row) for row in table)


if __name__ == '__main__':
    substr = 'ATACTCGGA'
    print(longest_repeating_subsequence(substr))
