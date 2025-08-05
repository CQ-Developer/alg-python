from abc import ABC, abstractmethod
from typing import override


class Solution(ABC):

    @abstractmethod
    def maximum_difference(self, nums: list[int]) -> int:
        pass


class SolutionA(Solution):

    @override
    def maximum_difference(self, nums: list[int]) -> int:
        mn, res = nums[0], 0
        for x in nums:
            if x < mn:
                mn = x
            else:
                res = max(res, x - mn)
        return res or -1
