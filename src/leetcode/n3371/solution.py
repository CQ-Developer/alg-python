from abc import ABC, abstractmethod
from typing import override
from collections import Counter
from math import inf


class Solution(ABC):

    @abstractmethod
    def get_largest_outlier(self, nums: list[int]) -> int:
        pass


class SolutionA(Solution):

    @override
    def get_largest_outlier(self, nums: list[int]) -> int:
        cnt, s = Counter(nums), sum(nums)
        ans = -inf
        for x in nums:
            y, m = divmod(s - x, 2)
            if m == 0 and y in cnt and (y != x or cnt[y] > 1):
                ans = max(ans, x)
        return ans
