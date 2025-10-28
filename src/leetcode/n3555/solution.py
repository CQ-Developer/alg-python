from abc import ABC, abstractmethod
from typing import override
from math import inf


class Solution(ABC):

    @abstractmethod
    def min_subarray_sort(self, nums: list[int], k: int) -> list[int]:
        pass


class SolutionA(Solution):

    @override
    def min_subarray_sort(self, nums: list[int], k: int) -> list[int]:
        n = len(nums)
        ans = [0] * (n - k + 1)
        for i in range(n - k + 1):
            l, r = -1, -1
            mn, mx = inf, -inf
            for p in range(k):
                if (nums[i + p]) < mx:
                    r = i + p
                else:
                    mx = nums[i + p]
                q = k - 1 - p
                if nums[i + q] > mn:
                    l = i + q
                else:
                    mn = nums[i + q]
            if r > -1:
                ans[i] = r - l + 1
        return ans
