from abc import ABC, abstractmethod
from typing import override


class Solution(ABC):

    @abstractmethod
    def count_odds(self, low: int, high: int) -> int:
        pass


class SolutionA(Solution):

    @override
    def count_odds(self, low: int, high: int) -> int:
        return sum(x & 1 for x in range(low, high + 1))


class SolutionB(Solution):

    @override
    def count_odds(self, low: int, high: int) -> int:
        return ((high + 1) >> 1) - (low >> 1)
