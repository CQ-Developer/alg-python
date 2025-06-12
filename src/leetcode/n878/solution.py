import math
from abc import ABC, abstractmethod
from typing import override


class Solution(ABC):

    @abstractmethod
    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
        pass


class SolutionA(Solution):

    @override
    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
        lcm = math.lcm(a, b)
        l, r = 1, min(a, b) * n
        while l + 1 < r:
            m = (l + r) // 2
            if m // a + m // b - m // lcm >= n:
                r = m
            else:
                l = m
        return r % 1_000_000_007
