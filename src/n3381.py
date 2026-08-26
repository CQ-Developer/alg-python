from abc import ABC, abstractmethod
from math import inf
from typing import override


class Solution(ABC):
    @abstractmethod
    def max_subarray_sum(self, nums: list[int], k: int) -> int:
        pass


class SolutionA(Solution):
    """ """

    @override
    def max_subarray_sum(self, nums: list[int], k: int) -> int:
        min_pre = [inf] * k
        pre = min_pre[-1] = 0
        ans = -inf
        for j, x in enumerate(nums):
            pre += x
            i = j % k
            ans = max(ans, pre - min_pre[i])
            min_pre[i] = min(min_pre[i], pre)
        return ans
