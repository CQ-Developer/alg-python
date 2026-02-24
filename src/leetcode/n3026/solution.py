from abc import ABC, abstractmethod
from typing import override
from math import inf
from collections import defaultdict


class Solution(ABC):

    @abstractmethod
    def maximum_subarray_sum(self, nums: list[int], k: int) -> int:
        pass


class SolutionA(Solution):

    @override
    def maximum_subarray_sum(self, nums: list[int], k: int) -> int:
        ans = -inf
        s = 0
        min_s = defaultdict(lambda: inf)
        for x in nums:
            ans = max(ans, s + x - min(min_s[x - k], min_s[x + k]))
            min_s[x] = min(min_s[x], s)
            s += x
        return ans if ans > -inf else 0
