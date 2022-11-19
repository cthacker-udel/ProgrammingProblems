from typing import List


class Solution:
    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
        ones_index = []
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    ones_index.append((i, j))
