from abc import ABC, abstractmethod
from typing import override


def guess(num: int) -> int:
    return 0


class Solution(ABC):

    @abstractmethod
    def guess_number(self, n: int) -> int:
        pass


class SolutionA(Solution):

    @override
    def guess_number(self, n: int) -> int:
        l, r = 1, n
        while l <= r:
            mid = (l + r) // 2
            g = guess(mid)
            if g == -1 or g == 0:
                r = mid - 1
            else:
                l = mid + 1
        return l
