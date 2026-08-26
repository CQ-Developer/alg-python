from abc import ABC, abstractmethod
from typing import override


class Solution(ABC):
    @abstractmethod
    def minimum_swaps(self, nums: list[int]) -> int:
        pass


class SolutionA(Solution):
    @override
    def minimum_swaps(self, nums: list[int]) -> int:
        ans = 0
        l, r = 0, len(nums) - 1
        while l < r:
            if nums[l] != 0:
                l += 1
            elif nums[r] == 0:
                r -= 1
            else:
                l += 1
                r -= 1
                ans += 1
        return ans
