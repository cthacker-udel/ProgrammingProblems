
from pprint import pprint


def diff_utility(str1: str, str2: str) -> None:
    table = []
    for _ in str1:
        table_row = []
        for __ in str2:
            table_row.append(0)
        table.append(table_row)
        table_row = []

    for i in range(len(str1)):
        for j in range(len(str2)):
            if str1[i] == str2[j]:
                table[i][j] = 0
            else:
                top_value, left_value, right_value, bottom_value = float(
                    'inf'), float('inf'), float('inf'), float('inf')
                if i > 0:
                    top_value = table[i - 1][j]
                if j > 0:
                    left_value = table[i][j - 1]
                if j < len(table[i]) - 1:
                    right_value = table[i][j + 1]
                if i < len(table) - 1:
                    bottom_value = table[i + 1][j]
                table[i][j] = min(top_value, left_value,
                                  right_value, bottom_value) + 1
    pprint(table)


if __name__ == '__main__':
    x = 'XMJYAUZ'
    y = 'XMJAATZ'
    diff_utility(x, y)
