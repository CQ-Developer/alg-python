from abc import ABC, abstractmethod
from typing import override


class Solution(ABC):

    @abstractmethod
    def find_peak_grid(self, mat: list[list[int]]) -> list[int]:
        pass


class SolutionA(Solution):

    @override
    def find_peak_grid(self, mat: list[list[int]]) -> list[int]:
        l, r = -1, len(mat) - 1
        while l + 1 < r:
            i = (l + r) // 2
            j = mat[i].index(max(mat[i]))
            if mat[i][j] > mat[i + 1][j]:
                r = i
            else:
                l = i
        return [r, mat[r].index(max(mat[r]))]
