from abc import ABC, abstractmethod
from typing import override


class Solution(ABC):

    @abstractmethod
    def valid_subarray_size(self, nums: list[int], threshold: int) -> int:
        pass


class SolutionA(Solution):

    @override
    def valid_subarray_size(self, nums: list[int], threshold: int) -> int:
        n = len(nums)

        stk = []
        left = [-1] * n
        for i, v in enumerate(nums):
            while stk and nums[stk[-1]] >= v:
                stk.pop()
            if stk:
                left[i] = stk[-1]
            stk.append(i)

        stk.clear()
        right = [n] * n
        for i in range(n - 1, -1, -1):
            while stk and nums[stk[-1]] >= nums[i]:
                stk.pop()
            if stk:
                right[i] = stk[-1]
            stk.append(i)

        for v, l, r in zip(nums, left, right):
            k = r - l - 1
            if v > threshold // k:
                return k

        return -1
