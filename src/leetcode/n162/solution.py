from abc import ABC, abstractmethod
from typing import override


class Solution(ABC):

    @abstractmethod
    def find_peak_element(self, nums: list[int]) -> int:
        pass


class SolutionA(Solution):

    @override
    def find_peak_element(self, nums: list[int]) -> int:
        l, r = -1, len(nums) - 1
        while l + 1 < r:
            i = (l + r) // 2
            if nums[i] > nums[i + 1]:
                r = i
            else:
                l = i
        return r
