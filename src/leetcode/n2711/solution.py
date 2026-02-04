from abc import ABC, abstractmethod
from typing import override


class Solution(ABC):

    @abstractmethod
    def difference_of_distinct_values(self, grid: list[list[int]]) -> list[list[int]]:
        pass


class SolutionA(Solution):

    @override
    def difference_of_distinct_values(self, grid: list[list[int]]) -> list[list[int]]:
        m, n = len(grid), len(grid[0])
        ans = [[0] * n for _ in range(m)]
        s = set()
        for k in range(1, m + n):
            mn, mx = max(n - k, 0), min(m + n - 1 - k, n - 1)
            s.clear()
            for j in range(mn, mx + 1):
                i = k + j - n
                ans[i][j] = len(s)
                s.add(grid[i][j])
            s.clear()
            for j in range(mx, mn - 1, -1):
                i = k + j - n
                ans[i][j] = abs(ans[i][j] - len(s))
                s.add(grid[i][j])
        return ans


class SolutionB(Solution):

    @override
    def difference_of_distinct_values(self, grid: list[list[int]]) -> list[list[int]]:
        m, n = len(grid), len(grid[0])
        ans = [[0] * n for _ in range(m)]
        for k in range(1, m + n):
            mn, mx = max(n - k, 0), min(m + n - 1 - k, n - 1)
            b = 0
            for j in range(mn, mx + 1):
                i = k + j - n
                ans[i][j] = b.bit_count()
                b |= 1 << grid[i][j]
            b = 0
            for j in range(mx, mn - 1, -1):
                i = k + j - n
                ans[i][j] = abs(ans[i][j] - b.bit_count())
                b |= 1 << grid[i][j]
        return ans
