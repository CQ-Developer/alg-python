from abc import ABC, abstractmethod
from typing import override


class Solution(ABC):

    @abstractmethod
    def count_complete_day_pairs(self, hours: list[int]) -> int:
        pass


class SolutionA(Solution):

    @override
    def count_complete_day_pairs(self, hours: list[int]) -> int:
        res = 0
        cnt = [0] * 24
        for hour in hours:
            res += cnt[(24 - (hour % 24)) % 24]
            cnt[hour % 24] += 1
        return res
