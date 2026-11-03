from abc import ABC, abstractmethod
from typing import override


class Solution(ABC):
    @abstractmethod
    def count_submatrices(self, grid: list[list[int]], k: int) -> int:
        pass


class SolutionA(Solution):
    @override
    def count_submatrices(self, grid: list[list[int]], k: int) -> int:
        cnt = 0
        m, n = len(grid), len(grid[0])
        s = [[0] * (n + 1) for _ in range(m + 1)]
        for i, row in enumerate(grid):
            for j, x in enumerate(row):
                s[i + 1][j + 1] = s[i + 1][j] + s[i][j + 1] - s[i][j] + x
                if s[i + 1][j + 1] <= k:
                    cnt += 1
        return cnt


class SolutionB(Solution):
    @override
    def count_submatrices(self, grid: list[list[int]], k: int) -> int:
        cnt = 0
        col_sum = [0] * len(grid[0])
        for row in grid:
            s = 0
            for j, x in enumerate(row):
                col_sum[j] += x
                s += col_sum[j]
                if s > k:
                    break
                cnt += 1
        return cnt
