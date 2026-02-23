from abc import ABC, abstractmethod
from typing import override
from itertools import accumulate


class Solution(ABC):

    @abstractmethod
    def find_max_length(self, nums: list[int]) -> int:
        pass


class SolutionA(Solution):

    @override
    def find_max_length(self, nums: list[int]) -> int:
        nums = [x * 2 - 1 for x in nums]
        ps = list(accumulate(nums, initial=0))
        tab = {}
        mx = 0
        for i, p in enumerate(ps):
            if p in tab:
                mx = max(mx, i - tab[p])
            else:
                tab[p] = i
        return mx


class SolutionB(Solution):

    def find_max_length(self, nums: list[int]) -> int:
        p = mx = 0
        tb = {0: -1}
        for i, x in enumerate(nums):
            p += x * 2 - 1
            if p in tb:
                mx = max(mx, i - tb[p])
            else:
                tb[p] = i
        return mx
