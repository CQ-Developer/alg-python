from abc import ABC, abstractmethod
from typing import override


class Solution(ABC):

    @abstractmethod
    def find_indices(self, nums: list[int], index_difference: int, value_difference: int) -> list[int]:
        pass


class SolutionA(Solution):

    @override
    def find_indices(self, nums: list[int], index_difference: int, value_difference: int) -> list[int]:
        a = b = 0
        for i in range(index_difference, len(nums)):
            j = i - index_difference
            if nums[j] < nums[a]:
                a = j
            elif nums[j] > nums[b]:
                b = j
            if nums[i] - nums[a] >= value_difference:
                return [a, i]
            if nums[b] - nums[i] >= value_difference:
                return [b, i]
        return [-1, -1]
