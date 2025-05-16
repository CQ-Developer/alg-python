from abc import ABC, abstractmethod
from typing import override


class Solution(ABC):

    @abstractmethod
    def minCapability(self, nums: list[int], k: int) -> int:
        pass


class SolutionA(Solution):

    @override
    def minCapability(self, nums: list[int], k: int) -> int:
        def check(mx: int) -> bool:
            f1, f2 = 0, 0
            for x in nums:
                if x > mx:
                    f1 = f2
                else:
                    f1, f2 = f2, max(f2, f1 + 1)
            return f2 >= k

        l, r = 0, max(nums)
        while l + 1 < r:
            m = (l + r) // 2
            if check(m):
                r = m
            else:
                l = m
        return r
