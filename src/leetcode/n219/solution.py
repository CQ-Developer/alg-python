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


class SolutionB(Solution):

    @override
    def contains_nearby_duplicate(self, nums: list[int], k: int) -> bool:
        s = set()
        for i, x in enumerate(nums):
            if x in s:
                return True
            s.add(x)
            if i >= k:
                s.remove(nums[i - k])
        return False
