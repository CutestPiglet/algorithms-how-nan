# coding: utf-8

"""
https://leetcode.com/problems/number-of-islands/
"""

from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        m, n, count = len(grid), len(grid[0]), 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    self.dfs(grid, i, j)
                    count += 1

        return count

    def dfs(self, grid, i, j):

        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] != '1':
            return

        grid[i][j] = '#'

        self.dfs(grid, i + 1, j)
        self.dfs(grid, i - 1, j)
        self.dfs(grid, i, j + 1)
        self.dfs(grid, i, j - 1)
