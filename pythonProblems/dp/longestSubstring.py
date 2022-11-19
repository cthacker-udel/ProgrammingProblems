from pprint import pprint

def longestSubstring(substr1: str, substr2: str) -> str:
    table = []
    for _ in substr1:
        table_row = []
        for __ in substr2:
            table_row.append(0)
        table.append(table_row)
        table_row = []
    
    for i in range(len(substr1)):
        for j in range(len(substr2)):
            if substr1[i] == substr2[j]:
                if i == 0:
                    table[i][j] = 1
                elif j == 0:
                    table[i][j] = 1
                else:
                    table[i][j] = table[i - 1][j - 1] + 1

    coords = []
    max_value = 0
    for eachrow in table:
        max_value = max(max_value, max(eachrow))
    
    for i in range(len(table)):
        for j in range(len(table[i])):
            if table[i][j] == max_value:
                coords.append((i, j))

    substrs = []
    for eachcoord in coords:
        x_ = eachcoord[1]
        y_ = eachcoord[0]
        substr = ''
        while table[y_][x_] != 0 and x_ >= 0 and y_ >= 0:
            substr += substr1[x_]
            x_ -= 1
            y_ -= 1
        substrs.append(substr)
    print(substrs)
    
    


if __name__ == '__main__':
    s1 = 'abab'
    s2 = 'baba'
    longestSubstring(s1, s2)