from abc import ABC, abstractmethod
from typing import override
from itertools import groupby
from bisect import bisect_left


class Solution(ABC):

    @abstractmethod
    def minLength(self, s: str, numOps: int) -> int:
        pass


class SolutionA(Solution):

    @override
    def minLength(self, s: str, numOps: int) -> int:
        n = len(s)

        def check(m: int) -> bool:
            if m == 1:
                cnt = sum((ord(c) ^ i) & 1 for i, c in enumerate(s))
                cnt = min(cnt, n - cnt)
            else:
                cnt = sum(len(list(g)) // (m + 1) for _, g in groupby(s))
            return cnt <= numOps

        return bisect_left(range(n), True, 1, key=check)
