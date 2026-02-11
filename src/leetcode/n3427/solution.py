from abc import ABC, abstractmethod
from typing import override
from itertools import accumulate


class Solution(ABC):

    @abstractmethod
    def subarray_sum(self, nums: list[int]) -> int:
        pass


class SolutionA(Solution):

    @override
    def subarray_sum(self, nums: list[int]) -> int:
        s = 0
        p = [0] * (len(nums) + 1)
        for i, x in enumerate(nums):
            p[i + 1] = p[i] + x
            s += p[i + 1] - p[max(0, i - x)]
        return s


class SolutionB(Solution):

    @override
    def subarray_sum(self, nums: list[int]) -> int:
        p = list(accumulate(nums, initial=0))
        return sum(p[i + 1] - p[max(0, i - x)] for i, x in enumerate(nums))
