from abc import ABC, abstractmethod
from typing import override


class Solution(ABC):

    @abstractmethod
    def search(self, nums: list[int], target: int) -> int:
        pass


class SolutionA(Solution):

    @override
    def search(self, nums: list[int], target: int) -> int:
        l, r = -1, len(nums)
        while l + 1 < r:
            i = (l + r) // 2
            if nums[i] > target:
                if target < nums[0] and nums[i] > nums[-1]:
                    l = i
                else:
                    r = i
            elif nums[i] < target:
                if target > nums[-1] and nums[i] < nums[0]:
                    r = i
                else:
                    l = i
            else:
                return i
        return -1
