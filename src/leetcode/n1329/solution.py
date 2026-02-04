from abc import ABC, abstractmethod
from typing import override


class Solution(ABC):

    @abstractmethod
    def diagonal_sort(self, mat: list[list[int]]) -> list[list[int]]:
        pass


class SolutionA(Solution):

    @override
    def diagonal_sort(self, mat: list[list[int]]) -> list[list[int]]:
        m, n = len(mat), len(mat[0])
        for k in range(1 - n, m):
            mn, mx = max(-k, 0), min(m - 1 - k, n - 1)
            arr = sorted(mat[j + k][j] for j in range(mn, mx + 1))
            for j in range(mn, mx + 1):
                mat[j + k][j] = arr[j - mn]
        return mat
