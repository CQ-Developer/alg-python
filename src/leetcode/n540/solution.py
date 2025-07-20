from abc import ABC, abstractmethod
from typing import override


class Solution(ABC):

    @abstractmethod
    def single_non_duplicate(self, nums: list[int]) -> int:
        pass


class SolutionA(Solution):

    @override
    def single_non_duplicate(self, nums: list[int]) -> int:
        result = 0
        for x in nums:
            result ^= x
        return result
