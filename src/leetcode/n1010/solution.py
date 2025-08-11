from abc import ABC, abstractmethod
from typing import override


class Solution(ABC):

    @abstractmethod
    def num_pairs_divisible_by_60(self, time: list[int]) -> int:
        pass


class SolutionA(Solution):

    @override
    def num_pairs_divisible_by_60(self, time: list[int]) -> int:
        res = 0
        cnt = [0] * 60
        for x in time:
            res += cnt[(60 - x % 60) % 60]
            cnt[x % 60] += 1
        return res
