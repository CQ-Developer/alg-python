from abc import ABC, abstractmethod
from bisect import bisect_left
from itertools import accumulate
from typing import override


class Solution(ABC):
    @abstractmethod
    def min_operations(self, nums: list[int], queries: list[int]) -> list[int]:
        pass


class SolutionA(Solution):
    @override
    def min_operations(self, nums: list[int], queries: list[int]) -> list[int]:
        n = len(nums)
        nums.sort()
        pre = list(accumulate(nums, initial=0))
        ans = []
        for q in queries:
            j = bisect_left(nums, q)
            left = q * j - pre[j]
            right = pre[-1] - pre[j] - q * (n - j)
            ans.append(left + right)
        return ans
