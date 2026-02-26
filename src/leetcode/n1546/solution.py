from abc import ABC, abstractmethod
from typing import override
from itertools import accumulate


class Solution(ABC):

    @abstractmethod
    def max_non_overlapping(self, nums: list[int], target: int) -> int:
        pass


class SolutionA(Solution):

    @override
    def max_non_overlapping(self, nums: list[int], target: int) -> int:
        p = mx = 0
        s = set([0])
        for x in nums:
            p += x
            if p - target in s:
                mx += 1
                s.clear()
            s.add(p)
        return mx


class SolutionB(Solution):

    @override
    def max_non_overlapping(self, nums: list[int], target: int) -> int:
        mx = 0
        s = set([0])
        for x in accumulate(nums):
            if x - target in s:
                mx += 1
                s.clear()
            s.add(x)
        return mx
