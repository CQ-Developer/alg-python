from abc import ABC, abstractmethod
from typing import override


class Solution(ABC):

    @abstractmethod
    def max_score_sightseeing_pair(self, values: list[int]) -> int:
        pass


class SolutionA(Solution):

    @override
    def max_score_sightseeing_pair(self, values: list[int]) -> int:
        mx, res = values[0], 0
        for i, v in enumerate(values[1:], 1):
            res = max(res, mx + v - i)
            mx = max(mx, v + i)
        return res
