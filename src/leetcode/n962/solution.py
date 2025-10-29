from abc import ABC, abstractmethod
from typing import override


class Solution(ABC):

    @abstractmethod
    def max_width_ramp(self, nums: list[int]) -> int:
        pass


class SolutionA(Solution):

    @override
    def max_width_ramp(self, nums: list[int]) -> int:
        stk = []
        for i, x in enumerate(nums):
            while not stk or x < nums[stk[-1]]:
                stk.append(i)
        mx = 0
        for j in range(len(nums) - 1, -1, -1):
            while stk and nums[j] >= nums[stk[-1]]:
                mx = max(mx, j - stk.pop())
        return mx
