import math
from abc import ABC, abstractmethod
from typing import override


class Solution(ABC):

    @abstractmethod
    def minimizeSet(self, divisor1: int, divisor2: int, uniqueCnt1: int, uniqueCnt2: int) -> int:
        pass


class SolutionA(Solution):

    @override
    def minimizeSet(self, divisor1: int, divisor2: int, uniqueCnt1: int, uniqueCnt2: int) -> int:
        lcm = math.lcm(divisor1, divisor2)

        def check(x: int) -> bool:
            a, b, c = x // divisor1, x // divisor2, x // lcm
            return x - a - b + c >= max(0, uniqueCnt1 - b + c) + max(0, uniqueCnt2 - a + c)

        l, r = 0, (uniqueCnt1 + uniqueCnt2) * 2 - 1
        while l < r:
            m = (l + r) // 2
            if check(m):
                r = m
            else:
                l = m + 1
        return r
