from abc import ABC, abstractmethod
from typing import override
from collections import defaultdict


class Solution(ABC):

    @abstractmethod
    def number_of_boomerangs(self, points: list[list[int]]) -> int:
        pass


class SolutionA(Solution):

    @override
    def number_of_boomerangs(self, points: list[list[int]]) -> int:
        ans = 0
        for x, y in points:
            cnt = defaultdict(int)
            for a, b in points:
                d = (x - a) ** 2 + (y - b) ** 2
                ans += cnt[d] * 2
                cnt[d] += 1
        return ans
