from abc import ABC, abstractmethod
from typing import override
from itertools import accumulate


class Solution(ABC):

    @abstractmethod
    def shift_distance(self, s: str, t: str, next_cost: list[int], previous_cost: list[int]) -> int:
        pass


class SolutionA(Solution):

    @override
    def shift_distance(self, s: str, t: str, next_cost: list[int], previous_cost: list[int]) -> int:
        nc = list(accumulate(next_cost + next_cost, initial=0))
        pc = list(accumulate(previous_cost + previous_cost))
        dst = 0
        for x, y in zip(s, t):
            x, y = ord(x) - 97, ord(y) - 97
            dst += min(nc[y + 26 if y < x else y] - nc[x], pc[x + 26 if x < y else x] - pc[y])
        return dst
