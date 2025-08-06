from abc import ABC, abstractmethod
from math import inf, isinf
from typing import override


class Solution(ABC):

    @abstractmethod
    def minimum_card_pickup(self, cards: list[int]) -> int:
        pass


class SolutionA(Solution):

    @override
    def minimum_card_pickup(self, cards: list[int]) -> int:
        latest = dict()
        res = inf
        for i, x in enumerate(cards):
            if x in latest:
                res = min(res, i - latest[x] + 1)
            latest[x] = i
        return -1 if isinf(res) else res
