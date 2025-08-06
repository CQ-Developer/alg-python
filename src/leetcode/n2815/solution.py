from abc import ABC, abstractmethod
from typing import override
from math import inf


class Solution(ABC):

    @abstractmethod
    def max_sum(self, nums: list[int]) -> int:
        pass


class SolutionA(Solution):

    @override
    def max_sum(self, nums: list[int]) -> int:
        res = -1
        ht = [-inf] * 10
        for x in nums:
            i = max(map(int, str(x)))
            res = max(res, ht[i] + x)
            ht[i] = max(ht[i], x)
        return res
