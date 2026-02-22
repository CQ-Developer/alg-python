from abc import ABC, abstractmethod
from typing import override
from collections import defaultdict


class Solution(ABC):

    @abstractmethod
    def beautiful_subarrays(self, nums: list[int]) -> int:
        pass


class SolutionA(Solution):

    @override
    def beautiful_subarrays(self, nums: list[int]) -> int:
        pre = ans = 0
        cnt = defaultdict(int)
        for x in nums:
            cnt[pre] += 1
            pre ^= x
            ans += cnt[pre]
        return ans
