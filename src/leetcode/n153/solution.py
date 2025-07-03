from abc import ABC, abstractmethod
from typing import override
from bisect import bisect_left


class Solution(ABC):

    @abstractmethod
    def find_min(self, nums: list[int]) -> int:
        pass


class SolutionA(Solution):

    @override
    def find_min(self, nums: list[int]) -> int:
        l, r = -1, len(nums) - 1
        while l + 1 < r:
            i = (l + r) // 2
            if nums[i] < nums[-1]:
                r = i
            else:
                l = i
        return nums[r]


class SolutionB(Solution):

    @override
    def find_min(self, nums: list[int]) -> int:
        i = bisect_left(range(len(nums) - 1), True, key=lambda j: nums[j] < nums[-1])
        return nums[i]
