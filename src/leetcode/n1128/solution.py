from abc import ABC, abstractmethod
from typing import override


class Solution(ABC):

    @abstractmethod
    def num_equiv_domino_pairs(self, dominoes: list[list[int]]) -> int:
        pass


class SolutionA(Solution):

    @override
    def num_equiv_domino_pairs(self, dominoes: list[list[int]]) -> int:
        res = 0
        cnt = [[0] * 10 for _ in range(10)]
        for i, j in dominoes:
            a, b = min(i, j), max(i, j)
            res += cnt[a][b]
            cnt[a][b] += 1
        return res
