from abc import ABC, abstractmethod
from typing import override


class Solution(ABC):

    @abstractmethod
    def find_diagonal_order(self, mat: list[list[int]]) -> list[int]:
        pass


class SolutionA(Solution):

    @override
    def find_diagonal_order(self, mat: list[list[int]]) -> list[int]:
        m, n = len(mat), len(mat[0])
        arr = []
        for k in range(0, m + n - 1):
            min_j, max_j = max(k - m + 1, 0), min(k, n - 1)
            if k % 2:
                for j in range(max_j, min_j - 1, -1):
                    arr.append(mat[k - j][j])
            else:
                for j in range(min_j, max_j + 1):
                    arr.append(mat[k - j][j])
        return arr
