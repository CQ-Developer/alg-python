from abc import ABC, abstractmethod
from typing import override


class Solution(ABC):

    @abstractmethod
    def my_sqrt(self, x: int) -> int:
        pass


class SolutionA(Solution):

    @override
    def my_sqrt(self, x: int) -> int:
        l, r = 0, (x + 1) // 2
        while l <= r:
            mid = (l + r) // 2
            if mid**2 <= x:
                l = mid + 1
            else:
                r = mid - 1
        return r
