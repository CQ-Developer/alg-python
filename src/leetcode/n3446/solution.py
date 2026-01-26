from abc import ABC, abstractmethod
from typing import override


class Solution(ABC):

    @abstractmethod
    def sort_matrix(self, grid: list[list[int]]) -> list[list[int]]:
        pass


class SolutionA(Solution):

    @override
    def sort_matrix(self, grid: list[list[int]]) -> list[list[int]]:
        n = len(grid)
        for k in range(1, n + n):
            mn, mx = max(n - k, 0), min(n + n - k - 1, n - 1)
            arr = [grid[k + j - n][j] for j in range(mn, mx + 1)]
            arr.sort(reverse=k >= n)
            for j, v in enumerate(arr, mn):
                grid[k + j - n][j] = v
        return grid
