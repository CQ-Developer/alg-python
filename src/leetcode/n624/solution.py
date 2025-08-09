from abc import ABC, abstractmethod
from typing import override


class Solution(ABC):

    @abstractmethod
    def max_distance(self, arrays: list[list[int]]) -> int:
        pass


class SolutionA(Solution):

    @override
    def max_distance(self, arrays: list[list[int]]) -> int:
        res, mn, mx = 0, arrays[0][0], arrays[0][-1]
        for arr in arrays[1:]:
            a, b = arr[0], arr[-1]
            res = max(res, max(mx - a, b - mn))
            mn = min(mn, a)
            mx = max(mx, b)
        return res
