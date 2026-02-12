from abc import ABC, abstractmethod
from typing import override
from itertools import accumulate


class Solution(ABC):

    @abstractmethod
    def max_absolute_sum(self, nums: list[int]) -> int:
        pass


class SolutionA(Solution):

    @override
    def max_absolute_sum(self, nums: list[int]) -> int:
        ans = mx = mn = 0
        for x in nums:
            mx = max(mx, 0) + x
            mn = min(mn, 0) + x
            ans = max(ans, mx, -mn)
        return ans


class SolutionB(Solution):

    @override
    def max_absolute_sum(self, nums: list[int]) -> int:
        s = list(accumulate(nums, initial=0))
        return max(s) - min(s)
