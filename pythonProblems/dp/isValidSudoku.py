from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for eachrow in board:
            row_values = []
            for eachvalue in eachrow:
                if eachvalue != '.' and eachvalue.isnumeric():
                    row_values.append(int(eachvalue))
            if len(set(row_values)) != len(row_values):
                print('row')
                return False
        for i in range(len(board)):
            column_values = []
            for j in range(len(board[i])):
                if board[j][i] != '.' and board[j][i].isnumeric():
                    column_values.append(int(board[j][i]))
            if len(set(column_values)) != len(column_values):
                print('col')
                return False
        for i in range(0, len(board) - 2, 3):
            grid_values = []
            # controls row traversal
            for j in range(0, len(board[i]) - 2, 3):
                grid_values = []
                for k in range(j, j + 3):
                    # controls inner row traversal
                    if board[i][k] != '.':
                        grid_values.append(int(board[i][k]))
                    if board[i + 1][k] != '.':
                        grid_values.append(int(board[i + 1][k]))
                    if board[i + 2][k] != '.':
                        grid_values.append(int(board[i + 2][k]))
                if len(set(grid_values)) != len(grid_values):
                    print('grid', grid_values)
                    return False
        return True


if __name__ == '__main__':
    board = [
            [".", ".", ".", ".", ".", ".", "5", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", "."],
            ["9", "3", ".", ".", "2", ".", "4", ".", "."],
            [".", ".", "7", ".", ".", ".", "3", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", "3", "4", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", "3", ".", ".", "."],
            [".", ".", ".", ".", ".", "5", "2", ".", "."]]
    sol = Solution()
    print(sol.isValidSudoku(board))
