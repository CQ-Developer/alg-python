from abc import ABC, abstractmethod
from typing import override


class Solution(ABC):

    @abstractmethod
    def number_of_right_trianles(self, grid: list[list[int]]) -> int:
        pass


class SolutionA(Solution):

    @override
    def number_of_right_trianles(self, grid: list[list[int]]) -> int:
        col_sum = [sum(col) - 1 for col in zip(*grid)]
        cnt = 0
        for row in grid:
            row_sum = sum(row) - 1
            cnt += row_sum * sum(col for x, col in zip(row, col_sum) if x)
        return cnt


class SolutionB(Solution):
    """
    SolutionA 的简化版
    """

    @override
    def number_of_right_trianles(self, grid: list[list[int]]) -> int:
        col_sum = [sum(col) - 1 for col in zip(*grid)]
        return sum((sum(row) - 1) * (sum(col for x, col in zip(row, col_sum) if x)) for row in grid)
