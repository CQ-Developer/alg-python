from abc import ABC, abstractmethod
from typing import override


class Solution(ABC):

    @abstractmethod
    def longest_alternating_subarray(self, nums: list[int], threshold: int) -> int:
        pass


class SolutionA(Solution):

    @override
    def longest_alternating_subarray(self, nums: list[int], threshold: int) -> int:
        a, n = 0, len(nums)
        for i, x in enumerate(nums):
            if x <= threshold and not (x & 1):
                j = i
                while i + 1 < n and nums[i + 1] <= threshold and (nums[i] & 1) != (nums[i + 1] & 1):
                    i += 1
                a = max(a, i - j + 1)
        return a
