from abc import ABC, abstractmethod
from math import inf
from typing import override


class Solution(ABC):
    @abstractmethod
    def max_score(self, grid: list[list[int]]) -> int:
        pass


class SolutionA(Solution):
    @override
    def max_score(self, grid: list[list[int]]) -> int:
        ans = -inf
        m, n = len(grid), len(grid[0])
        f = [[inf] * (n + 1) for _ in range(m + 1)]
        for i, row in enumerate(grid):
            for j, x in enumerate(row):
                mn = min(f[i + 1][j], f[i][j + 1])
                ans = max(ans, x - mn)
                f[i + 1][j + 1] = min(mn, x)
        return int(ans)


class SolutionB(Solution):
    @override
    def max_score(self, grid: list[list[int]]) -> int:
        ans = -inf
        col_min = [inf] * len(grid[0])
        for row in grid:
            pre_min = inf
            for j, x in enumerate(row):
                ans = max(ans, x - min(pre_min, col_min[j]))
                col_min[j] = min(col_min[j], x)
                pre_min = min(pre_min, col_min[j])
        return int(ans)
