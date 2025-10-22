from abc import ABC, abstractmethod
from typing import override


class Solution(ABC):

    @abstractmethod
    def minimum_operations(self, grid: list[list[int]]) -> int:
        pass


class SolutionA(Solution):

    @override
    def minimum_operations(self, grid: list[list[int]]) -> int:
        ops = 0
        for col in zip(*grid):
            pre = -1
            for x in col:
                ops += max(0, pre + 1 - x)
                pre = max(x, pre + 1)
        return ops
