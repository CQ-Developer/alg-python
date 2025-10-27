from abc import ABC, abstractmethod
from typing import override


class Solution(ABC):

    @abstractmethod
    def binary_searchable_numbers(self, nums: list[int]) -> int:
        pass


class SolutionA(Solution):

    @override
    def binary_searchable_numbers(self, nums: list[int]) -> int:
        n = len(nums)
        cnt = [1] * n
        mx, mn = -(10**5), 10**5
        for i, x in enumerate(nums):
            if x < mx:
                cnt[i] = 0
            else:
                mx = x
        ans = 0
        for i in range(n - 1, -1, -1):
            if nums[i] > mn:
                cnt[i] = 0
            else:
                mn = nums[i]
            ans += cnt[i]
        return ans
