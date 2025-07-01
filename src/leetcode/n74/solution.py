from abc import ABC, abstractmethod
from typing import override


class Solution(ABC):

    @abstractmethod
    def search_matrix(self, matrix: list[list[int]], target: int) -> bool:
        pass


class SolutionA(Solution):

    @override
    def search_matrix(self, matrix: list[list[int]], target: int) -> bool:
        for row in matrix:
            l, r = -1, len(row)
            while l + 1 < r:
                i = (l + r) // 2
                if row[i] == target:
                    return True
                if row[i] < target:
                    l = i
                else:
                    r = i
        return False
