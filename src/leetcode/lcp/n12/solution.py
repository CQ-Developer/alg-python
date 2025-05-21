from abc import ABC, abstractmethod
from typing import override
from bisect import bisect_left


class Solution(ABC):

    @abstractmethod
    def minTime(self, time: list[int], m: int) -> int:
        pass


class SolutionA(Solution):

    @override
    def minTime(self, time: list[int], m: int) -> int:
        def check(mx: int) -> bool:
            p, s, d = 0, 0, 1
            for t in time:
                if s + t - max(p, t) <= mx:
                    s += t
                    p = max(p, t)
                else:
                    s = p = t
                    d += 1
            return d <= m

        l, r = -1, sum(time)
        while l + 1 < r:
            mid = (l + r) // 2
            if check(mid):
                r = mid
            else:
                l = mid
        return r


class SolutionB(Solution):

    @override
    def minTime(self, time: list[int], m: int) -> int:
        def check(mx: int) -> bool:
            p, s, d = 0, 0, 1
            for t in time:
                if s + t - max(p, t) <= mx:
                    s += t
                    p = max(p, t)
                else:
                    s = p = t
                    d += 1
            return d <= m

        return bisect_left(range(sum(time)), True, key=check)
