from abc import ABC, abstractmethod
from typing import override


class Solution(ABC):

    @abstractmethod
    def min_operations(self, nums: list[int]) -> int:
        pass


class SolutionA(Solution):

    @override
    def min_operations(self, nums: list[int]) -> int:
        ops = 0
        stk = []
        for x in nums:
            while stk and x < stk[-1]:
                stk.pop()
                ops += 1
            if not stk or x != stk[-1]:
                stk.append(x)
        return ops + len(stk) - (stk[0] == 0)


class SolutionB(Solution):

    @override
    def min_operations(self, nums: list[int]) -> int:
        ops, k = 0, -1
        for x in nums:
            while k > -1 and x < nums[k]:
                k -= 1
                ops += 1
            if k == -1 or x != nums[k]:
                k += 1
                nums[k] = x
        return ops + k + (nums[0] > 0)
