from abc import ABC, abstractmethod
from typing import override
from collections import defaultdict


class Solution(ABC):

    @abstractmethod
    def subarrays_div_by_k(self, nums: list[int], k: int) -> int:
        pass


class SolutionA(Solution):

    @override
    def subarrays_div_by_k(self, nums: list[int], k: int) -> int:
        pre = ans = 0
        cnt = defaultdict(int)
        for x in nums:
            cnt[pre] += 1
            pre = (pre + x) % k
            ans += cnt[pre]
        return ans


class SolutionB(Solution):

    @override
    def subarrays_div_by_k(self, nums: list[int], k: int) -> int:
        pre = ans = 0
        cnt = [0] * k
        for x in nums:
            cnt[pre] += 1
            pre = (pre + x) % k
            ans += cnt[pre]
        return ans
