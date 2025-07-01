from abc import ABC, abstractmethod
from typing import override
from bisect import bisect_left


def is_bad_version(version: int) -> bool:
    return False


class Solution(ABC):

    @abstractmethod
    def first_bad_version(self, n: int) -> int:
        pass


class SolutionA(Solution):

    @override
    def first_bad_version(self, n: int) -> int:
        l, r = 1, n
        while l <= r:
            i = (l + r) // 2
            if is_bad_version(i):
                r = i - 1
            else:
                l = i + 1
        return l


class SolutionB(Solution):

    @override
    def first_bad_version(self, n: int) -> int:
        return bisect_left(range(n), True, key=is_bad_version)
