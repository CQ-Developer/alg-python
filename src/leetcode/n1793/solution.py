from abc import ABC, abstractmethod
from typing import override


class Solution(ABC):

    @abstractmethod
    def maximum_score(self, nums: list[int], k: int) -> int:
        pass


class SolutionA(Solution):

    @override
    def maximum_score(self, nums: list[int], k: int) -> int:
        n = len(nums)
        left = [-1] * n
        stk = []
        for i, x in enumerate(nums):
            while stk and x <= nums[stk[-1]]:
                stk.pop()
            if stk:
                left[i] = stk[-1]
            stk.append(i)
        stk.clear()
        right = [n] * n
        for i in range(n - 1, -1, -1):
            while stk and nums[i] <= nums[stk[-1]]:
                stk.pop()
            if stk:
                right[i] = stk[-1]
            stk.append(i)
        mx = 0
        for h, i, j in zip(nums, left, right):
            if i < k < j:
                mx = max(mx, h * (j - i - 1))
        return mx


class SolutionB(Solution):

    @override
    def maximum_score(self, nums: list[int], k: int) -> int:
        n = len(nums)
        mx = h = nums[k]
        i = j = k
        for _ in range(n - 1):
            if j == n - 1 or i > 0 and nums[i - 1] > nums[j + 1]:
                i -= 1
                h = min(h, nums[i])
            else:
                j += 1
                h = min(h, nums[j])
            mx = max(mx, h * (j - i + 1))
        return mx
