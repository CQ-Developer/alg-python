from abc import ABC, abstractmethod
from typing import override
from collections import defaultdict


class Solution(ABC):

    @abstractmethod
    def subarray_sum(self, nums: list[int], k: int) -> int:
        pass


class SolutionA(Solution):

    @override
    def subarray_sum(self, nums: list[int], k: int) -> int:
        ans = pre = 0
        cnt = defaultdict(int)
        for x in nums:
            cnt[pre] += 1
            pre += x
            ans += cnt[pre - k]
        return ans
