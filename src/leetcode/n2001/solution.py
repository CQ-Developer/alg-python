from abc import ABC, abstractmethod
from typing import override


class Solution(ABC):

    @abstractmethod
    def interchangeable_rectangles(self, rectangles: list[list[int]]) -> int:
        pass


class SolutionA(Solution):

    @override
    def interchangeable_rectangles(self, rectangles: list[list[int]]) -> int:
        result = 0
        h = dict()
        for rec in rectangles:
            k = rec[0] / rec[1]
            x = h.get(k, 0)
            result += x
            h[k] = x + 1
        return result
