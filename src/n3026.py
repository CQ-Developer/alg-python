import abc
import math
import typing
from collections import defaultdict


class Solution(abc.ABC):
    """
    https://leetcode.cn/problems/maximum-good-subarray-sum/description/
    """

    @abc.abstractmethod
    def maximum_subarray_sum(self, nums: list[int], k: int) -> int:
        pass


class SolutionA(Solution):
    """
    前缀和
    """

    @typing.override
    def maximum_subarray_sum(self, nums: list[int], k: int) -> int:
        s = 0
        a = -math.inf
        min_s = defaultdict(lambda: math.inf)
        for x in nums:
            a = max(a, s + x - min(min_s[x - k], min_s[x + k]))
            min_s[x] = min(min_s[x], s)
            s += x
        return int(a) if a > -math.inf else 0
