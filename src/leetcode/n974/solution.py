from abc import ABC, abstractmethod
from collections import defaultdict
from itertools import accumulate
from typing import override


class Solution(ABC):
    """
    和可被K整除的子数组
    """

    @abstractmethod
    def subarrays_div_by_k(self, nums: list[int], k: int) -> int:
        pass


class SolutionA(Solution):
    """
    前缀和
    """

    @override
    def subarrays_div_by_k(self, nums: list[int], k: int) -> int:
        ans = 0
        cnt = defaultdict(int)
        for x in accumulate(nums, initial=0):
            ans += cnt[x % k]
            cnt[x % k] += 1
        return ans


class SolutionB(Solution):
    """
    前缀和: 一次遍历
    """

    @override
    def subarrays_div_by_k(self, nums: list[int], k: int) -> int:
        cnt = defaultdict(int)
        ans = pre = 0
        for x in nums:
            cnt[pre] += 1
            pre = (pre + x) % k
            ans += cnt[pre]
        return ans


class SolutionC(Solution):
    """
    前缀和: 数组代替hash表
    """

    @override
    def subarrays_div_by_k(self, nums: list[int], k: int) -> int:
        cnt = [0] * k
        ans = pre = 0
        for x in nums:
            cnt[pre] += 1
            pre = (pre + x) % k
            ans += cnt[pre]
        return ans
