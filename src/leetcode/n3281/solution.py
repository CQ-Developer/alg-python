from abc import ABC, abstractmethod
from typing import override


class Solution(ABC):

    @abstractmethod
    def maxPossibleScore(self, start: list[int], d: int) -> int:
        pass


class SolutionA(Solution):

    @override
    def maxPossibleScore(self, start: list[int], d: int) -> int:
        def check(m: int) -> bool:
            p = -m
            for s in start:
                if p + m > s + d:
                    return False
                p = s if p + m <= s else p + m
            return True

        start.sort()
        l, r = 0, start[-1] + d
        while l <= r:
            m = (l + r) // 2
            if check(m):
                l = m + 1
            else:
                r = m - 1
        return r
