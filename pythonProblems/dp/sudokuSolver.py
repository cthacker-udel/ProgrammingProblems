from pprint import pprint
from typing import List


class Solution:
    """
    """

    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        for i in range(0, len(board) - 2, 3):
            grid_values = []
            # controls row traversal
            for j in range(0, len(board[i]) - 2, 3):
                grid_values = []
                for k in range(j, j + 3):
                    # controls inner row traversal
                    grid_values.append([board[i][k], (i, k)])
                    grid_values.append([board[i + 1][k], (i + 1, k)])
                    grid_values.append([board[i + 2][k], (i + 2, k)])
                for eachcoord in grid_values:
                    if eachcoord[0] == '.':
                        coord_y = eachcoord[1][0]
                        coord_x = eachcoord[1][1]
                        # analyze column, row, and then grid values
                        for eachnum in range(1, 10):
                            if len([x for x in grid_values if x[0] == str(eachnum)]) == 0:
                                # number is not in grid, analyze row values
                                row_values = []
                                for eachnumber in board[coord_y]:
                                    if eachnumber != '.':
                                        row_values.append(eachnumber)
                                if eachnum not in row_values:
                                    col_values = []
                                    for eachrow in board:
                                        if eachrow[coord_x] != '.':
                                            col_values.append(
                                                eachrow[coord_x])
                                    if str(eachnum) not in col_values:
                                        board[coord_y][coord_x] = str(eachnum)
                                        eachcoord[0] = str(eachnum)
                                        break
                                else:
                                    break


if __name__ == '__main__':
    sol = Solution()
    bd = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    sol.solveSudoku(bd)
    pprint(bd)
