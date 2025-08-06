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


class SolutionB(Solution):

    @override
    def minimum_card_pickup(self, cards: list[int]) -> int:
        s = set()
        l, res = 0, inf
        for r in range(len(cards)):
            while cards[r] in s:
                res = min(res, r - l + 1)
                s.remove(cards[l])
                l += 1
            s.add(cards[r])
        return -1 if isinf(res) else res
