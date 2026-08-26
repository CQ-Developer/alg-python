from abc import ABC, abstractmethod
from itertools import accumulate
from typing import override


class Solution(ABC):
    @abstractmethod
    def max_frequency_score(self, nums: list[int], k: int) -> int:
        pass


class SolutionA(Solution):
    """
    前缀和 + 划窗
    """

    @override
    def max_frequency_score(self, nums: list[int], k: int) -> int:
        n = len(nums)

        nums.sort()
        s = list(accumulate(nums, initial=0))

        def sum_distance(l: int, r: int) -> int:
            i = (l + r) // 2
            ls = nums[i] * (i - l) - (s[i] - s[l])
            rs = s[r + 1] - s[i + 1] - nums[i] * (r - i)
            return ls + rs

        a = l = 0
        for r in range(n):
            while sum_distance(l, r) > k:
                l += 1
            a = max(a, r - l + 1)
        return a


class SolutionB(Solution):
    """
    划窗
    """

    def max_frequency_score(self, nums: list[int], k: int) -> int:
        nums.sort()
        a = l = s = 0
        for r, x in enumerate(nums):
            s += x - nums[(l + r) // 2]
            while s > k:
                s += nums[l] - nums[(l + r + 1) // 2]
                l += 1
            a = max(a, r - l + 1)
        return a
