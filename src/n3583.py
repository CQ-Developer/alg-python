from abc import ABC, abstractmethod
from collections import Counter, defaultdict
from typing import override


class Solution(ABC):
    @abstractmethod
    def special_triplets(self, nums: list[int]) -> int:
        pass


class SolutionA(Solution):
    @override
    def special_triplets(self, nums: list[int]) -> int:
        ans = 0
        pre, suf = defaultdict(int), Counter(nums)
        for x in nums:
            suf[x] -= 1
            ans += pre[x * 2] * suf[x * 2]
            pre[x] += 1
        return ans % (10**9 + 7)
