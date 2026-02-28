from abc import ABC, abstractmethod
from typing import override
from math import inf


class Solution(ABC):

    @abstractmethod
    def max_subarray_sum(self, nums: list[int], k: int) -> int:
        pass


class SolutionA(Solution):

    @override
    def max_subarray_sum(self, nums: list[int], k: int) -> int:
        min_pre = [inf] * (k + 1)
        pre = min_pre[0] = 0
        ans = -inf
        for i, x in enumerate(nums, start=1):
            pre += x
            j = i % k
            ans = max(ans, pre - min_pre[j])
            min_pre[j] = min(pre, min_pre[j])
        return ans
