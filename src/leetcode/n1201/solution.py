from abc import ABC, abstractmethod
from typing import override
from math import lcm


class Solution(ABC):

    @abstractmethod
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        pass


class SolutionA(Solution):

    @override
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        ab, bc, ca, abc = lcm(a, b), lcm(b, c), lcm(c, a), lcm(a, b, c)
        m = min(a, b, c)
        l, r = m, m * n
        while l < r:
            x = (l + r) // 2
            if x // a + x // b + x // c - x // ab - x // bc - x // ca + x // abc >= n:
                r = x
            else:
                l = x + 1
        return r
