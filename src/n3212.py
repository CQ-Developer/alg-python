from abc import ABC, abstractmethod
from typing import override


class Solution(ABC):
    @abstractmethod
    def number_of_submatrices(self, grid: list[list[str]]) -> int:
        pass


class SolutionA(Solution):
    @override
    def number_of_submatrices(self, grid: list[list[str]]) -> int:
        cnt = 0
        m, n = len(grid), len(grid[0])
        s = [[[0, 0] for _ in range(n + 1)] for _ in range(m + 1)]
        for i, row in enumerate(grid):
            for j, c in enumerate(row):
                s[i + 1][j + 1][0] = s[i + 1][j][0] + s[i][j + 1][0] - s[i][j][0]
                s[i + 1][j + 1][1] = s[i + 1][j][1] + s[i][j + 1][1] - s[i][j][1]
                if c != ".":
                    s[i + 1][j + 1][1 & ord(c)] += 1
                if s[i + 1][j + 1][0] > 0 and s[i + 1][j + 1][0] == s[i + 1][j + 1][1]:
                    pass
                if 0 < s[i + 1][j + 1][0] == s[i + 1][j + 1][1]:
                    cnt += 1
        return cnt


class SolutionB(Solution):
    @override
    def number_of_submatrices(self, grid: list[list[str]]) -> int:
        cnt = 0
        col_sum = [[0, 0] for _ in grid[0]]
        for row in grid:
            s1 = s2 = 0
            for j, c in enumerate(row):
                if c != ".":
                    col_sum[j][1 & ord(c)] += 1
                s1 += col_sum[j][0]
                s2 += col_sum[j][1]
                if 0 < s1 == s2:
                    cnt += 1
        return cnt
