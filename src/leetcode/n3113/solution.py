from abc import ABC, abstractmethod
from typing import override
from math import inf


class Solution(ABC):

    @abstractmethod
    def numberOfSubarrays(self, nums: list[int]) -> int:
        pass


class SolutionA(Solution):

    @override
    def numberOfSubarrays(self, nums: list[int]) -> int:
        n = len(nums)
        stk = [[inf, 0]]
        for num in nums:
            while num > stk[-1][0]:
                stk.pop()
            if num == stk[-1][0]:
                n += stk[-1][1]
                stk[-1][1] += 1
            else:
                stk.append([num, 1])
        return n
