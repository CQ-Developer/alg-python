from abc import ABC, abstractmethod
from typing import override


class Solution(ABC):

    @abstractmethod
    def my_pow(self, x: float, n: int) -> float:
        pass


class SolutionA(Solution):

    @override
    def my_pow(self, x: float, n: int) -> float:
        if n < 0:
            n = -n
            x = 1 / x
        p = 1.0
        while n > 0:
            if (n & 1) == 1:
                p *= x
            x *= x
            n >>= 1
        return p
