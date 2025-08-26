from abc import ABC, abstractmethod
from typing import override


class Solution(ABC):

    @abstractmethod
    def next_greater_elements(self, nums: list[int]) -> list[int]:
        pass


class SolutionA(Solution):

    @override
    def next_greater_elements(self, nums: list[int]) -> list[int]:
        n = len(nums)
        stk, res = [], [-1] * n
        for i in range(n * 2 - 1, -1, -1):
            x = nums[i % n]
            while stk and x >= stk[-1]:
                stk.pop()
            if i < n and stk:
                res[i] = stk[-1]
            stk.append(x)
        return res


class SolutionB(Solution):

    @override
    def next_greater_elements(self, nums: list[int]) -> list[int]:
        n = len(nums)
        stk, res = [], [-1] * n
        for i in range(n * 2):
            x = nums[i % n]
            while stk and x > nums[stk[-1]]:
                res[stk.pop()] = x
            if i < n:
                stk.append(i)
        return res
