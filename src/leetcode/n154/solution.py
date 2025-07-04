from abc import ABC, abstractmethod
from typing import override


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
            if nums[i] < nums[r]:
                r = i
            elif nums[i] > nums[r]:
                l = i
            else:
                r -= 1
        return nums[r]
