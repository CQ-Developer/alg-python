from abc import ABC, abstractmethod
from typing import override


class Solution(ABC):

    @abstractmethod
    def two_sum(self, nums: list[int], target: int) -> list[int]:
        pass


class SolutionA(Solution):

    @override
    def two_sum(self, nums: list[int], target: int) -> list[int]:
        caching = dict()
        for i, num in enumerate(nums):
            if target - num in caching:
                return [caching[target - num], i]
            caching[num] = i
        return []
