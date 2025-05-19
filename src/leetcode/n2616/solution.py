from abc import ABC, abstractmethod
from typing import override


class Solution(ABC):

    @abstractmethod
    def minimizeMax(self, nums: list[int], p: int) -> int:
        pass


class SolutionA(Solution):

    @override
    def minimizeMax(self, nums: list[int], p: int) -> int:
        nums.sort()

        def check(mx: int) -> bool:
            i = cnt = 0
            while i + 1 < len(nums):
                if nums[i + 1] - nums[i] <= mx:
                    cnt += 1
                    i += 1
                i += 1
            return cnt >= p

        l, r = 0, nums[-1] - nums[0]
        while l < r:
            m = (l + r) // 2
            if check(m):
                r = m
            else:
                l = m + 1
        return r
