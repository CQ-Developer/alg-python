from abc import ABC, abstractmethod
from typing import override


class Solution(ABC):

    @abstractmethod
    def total_steps(self, nums: list[int]) -> int:
        pass


class SolutionA(Solution):
    """
    单调栈(从左向右)
    """

    @override
    def total_steps(self, nums: list[int]) -> int:
        stp = 0
        stk = []
        for x in nums:
            mx = 0
            while stk and x >= stk[-1][0]:
                mx = max(mx, stk.pop()[1])
            if stk:
                mx += 1
            stp = max(stp, mx)
            stk.append((x, mx))
        return stp


class SolutionB(Solution):
    """
    单调栈(从右向左)
    """

    @override
    def total_steps(self, nums: list[int]) -> int:
        n = len(nums)
        s, a = [], [0] * n
        for i in range(n - 1, -1, -1):
            while s and nums[i] > nums[s[-1]]:
                a[i] = max(a[s.pop()], a[i] + 1)
            s.append(i)
        return max(a)
