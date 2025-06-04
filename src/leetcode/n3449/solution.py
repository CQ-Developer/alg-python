from abc import ABC, abstractmethod
from typing import override


class Solution(ABC):

    @abstractmethod
    def maxScore(self, points: list[int], m: int) -> int:
        pass


class SolutionA(Solution):

    @override
    def maxScore(self, points: list[int], m: int) -> int:
        n = len(points)

        def check(low: int) -> bool:
            p, r = 0, m
            for i, x in enumerate(points):
                k = (low - 1) // x + 1 - p
                if i == n - 1 and k <= 0:
                    break
                if k < 1:
                    k = 1
                r -= 2 * k - 1
                if r < 0:
                    return False
                p = k - 1
            return True

        l, r = 0, (m + 1) // 2 * min(points) + 1
        while l + 1 < r:
            mid = (l + r) // 2
            if check(mid):
                l = mid
            else:
                r = mid
        return l
