from abc import ABC, abstractmethod
from typing import override
from sortedcontainers import SortedList
from math import inf


class Solution(ABC):

    @abstractmethod
    def find_132_pattern(self, nums: list[int]) -> bool:
        pass


class SolutionA(Solution):

    @override
    def find_132_pattern(self, nums: list[int]) -> bool:
        a = nums[0]
        c = SortedList(nums[2:])
        for i, b in enumerate(nums[1:-1], 1):
            if a < b:
                j = c.bisect_right(a)
                if j < len(c) and c[j] < b:
                    return True
            a = min(a, b)
            c.remove(nums[i + 1])
        return False


class SolutionB(Solution):

    @override
    def find_132_pattern(self, nums: list[int]) -> bool:
        stk = [nums[-1]]
        max_k = -inf
        for x in reversed(nums[:-1]):
            if x < max_k:
                return True
            while stk and x > stk[-1]:
                max_k = stk.pop()
            if x > max_k:
                stk.append(x)
        return False
