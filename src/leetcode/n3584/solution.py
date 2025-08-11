from abc import ABC, abstractmethod
from typing import override
from math import inf


class Solution(ABC):

    @abstractmethod
    def maximum_product(self, nums: list[int], m: int) -> int:
        pass


class SolutionA(Solution):

    @override
    def maximum_product(self, nums: list[int], m: int) -> int:
        res, mn, mx = -inf, inf, -inf
        for i, x in enumerate(nums[m - 1:], m - 1):
            mn = min(mn, nums[i - m + 1])
            mx = max(mx, nums[i - m + 1])
            res = max(res, mn * x, mx * x)
        return res
