from abc import ABC, abstractmethod
from typing import override
from math import inf


class Solution(ABC):

    @abstractmethod
    def max_subarray(self, nums: list[int]) -> int:
        pass


class SolutionA(Solution):

    @override
    def max_subarray(self, nums: list[int]) -> int:
        ans = -inf
        pre = min_pre = 0
        for x in nums:
            pre += x
            ans = max(ans, pre - min_pre)
            min_pre = min(min_pre, pre)
        return ans


class SolutionB(Solution):

    @override
    def max_subarray(self, nums: list[int]) -> int:
        n = len(nums)
        f = [0] * n
        f[0] = nums[0]
        for i in range(1, n):
            f[i] = max(f[i - 1], 0) + nums[i]
        return max(f)


class SolutionC(Solution):

    @override
    def max_subarray(self, nums: list[int]) -> int:
        """
        空间压缩
        """
        mx, f = -inf, 0
        for x in nums:
            f = max(f, 0) + x
            mx = max(mx, f)
        return mx
