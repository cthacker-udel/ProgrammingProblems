from __future__ import annotations
from typing import List, Optional


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        base_len = len(matrix)
        col_len = len(matrix[0])
        range_base = range(base_len)
        range_col = range(col_len)
        longest_paths = [[1] * col_len for x in range_base]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                self.find_longest_path(matrix, longest_paths, i, j)
        max_len = 1
        for each_row in longest_paths:
            max_len = max(max_len, max(each_row))
        return max_len

    def find_longest_path(
        self,
        matrix: List[List[int]],
        dfs_table: List[List[int]],
        row: int,
        col: int,
        current_length: int = 1,
    ) -> None:
        if row != -1 and col != -1 and row < len(matrix) and col < len(matrix[0]):
            current_element = matrix[row][col]
            left_element = matrix[row][col - 1] if col > 0 else 1
            right_element = matrix[row][col + 1] if col < len(matrix[0]) - 1 else 1
            bottom_element = matrix[row + 1][col] if row < len(matrix) - 1 else 1
            top_element = matrix[row - 1][col] if row > 0 else 1

            if dfs_table[row][col] != 1:
                return

            if top_element > current_element:
                self.find_longest_path(
                    matrix, dfs_table, row - 1, col, current_length + 1
                )  # top
            if bottom_element > current_element:
                self.find_longest_path(
                    matrix, dfs_table, row + 1, col, current_length + 1
                )
            if right_element > current_element:
                self.find_longest_path(
                    matrix, dfs_table, row, col + 1, current_length + 1
                )
            if left_element > current_element:
                self.find_longest_path(
                    matrix, dfs_table, row, col - 1, current_length + 1
                )

            dfs_left = (
                dfs_table[row][col - 1]
                if col > 0 and matrix[row][col - 1] > matrix[row][col]
                else 0
            )
            dfs_right = (
                dfs_table[row][col + 1]
                if col < len(matrix[0]) - 1 and matrix[row][col + 1] > matrix[row][col]
                else 0
            )
            dfs_bottom = (
                dfs_table[row + 1][col]
                if row < len(matrix) - 1 and matrix[row + 1][col] > matrix[row][col]
                else 0
            )
            dfs_top = (
                dfs_table[row - 1][col]
                if row > 0 and matrix[row - 1][col] > matrix[row][col]
                else 0
            )
            dfs_table[row][col] = (
                max(dfs_left, max(dfs_right, max(dfs_bottom, dfs_top))) + 1
            )


if __name__ == "__main__":
    sol = Solution()
    a = [[9, 9, 4], [6, 6, 8], [2, 1, 1]]
    b = [[3, 4, 5], [3, 2, 6], [2, 2, 1]]
    c = [[1]]
    print(sol.longestIncreasingPath(a))
    print(sol.longestIncreasingPath(b))
    print(sol.longestIncreasingPath(c))
