from abc import ABC, abstractmethod
from typing import override
from itertools import accumulate
import operator


class Solution(ABC):

    @abstractmethod
    def xor_queries(self, arr: list[int], queries: list[list[int]]) -> list[int]:
        pass


class SolutionA(Solution):

    @override
    def xor_queries(self, arr: list[int], queries: list[list[int]]) -> list[int]:
        p = list(accumulate(arr, operator.xor, initial=0))
        return [p[r + 1] ^ p[l] for l, r in queries]
