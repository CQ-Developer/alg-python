from abc import ABC, abstractmethod
from typing import override


class Solution(ABC):

    @abstractmethod
    def num_identical_pairs(self, nums: list[int]) -> int:
        pass


class SolutionA(Solution):

    @override
    def num_identical_pairs(self, nums: list[int]) -> int:
        res = 0
        caching = dict()
        for x in nums:
            p = caching.get(x, 0)
            res += p
            caching[x] = p + 1
        return res
