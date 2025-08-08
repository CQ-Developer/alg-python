from abc import ABC, abstractmethod
from collections import Counter
from typing import override


class Solution(ABC):

    @abstractmethod
    def count_trapezoids(self, points: list[list[int]]) -> int:
        pass


class SolutionA(Solution):

    @override
    def count_trapezoids(self, points: list[list[int]]) -> int:
        cnt = Counter(y for _, y in points)
        res = p = 0
        for x in cnt.values():
            k = x * (x - 1) // 2
            res += k * p
            p += k
        return res % 1000000007
