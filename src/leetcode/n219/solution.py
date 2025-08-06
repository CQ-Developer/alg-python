from abc import ABC, abstractmethod
from typing import override


class Solution(ABC):

    @abstractmethod
    def contains_nearby_duplicate(self, nums: list[int], k: int) -> bool:
        pass


class SolutionA(Solution):

    @override
    def contains_nearby_duplicate(self, nums: list[int], k: int) -> bool:
        latest = dict()
        for i, x in enumerate(nums):
            if x in latest and i - latest[x] <= k:
                return True
            latest[x] = i
        return False
