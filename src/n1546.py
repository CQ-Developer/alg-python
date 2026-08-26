from abc import ABC, abstractmethod
from itertools import accumulate
from typing import override


class Solution(ABC):
    """
    求非空不重叠子数组最大数目
    """

    @abstractmethod
    def max_non_overlapping(self, nums: list[int], target: int) -> int:
        pass


class SolutionA(Solution):
    """
    前缀和 + 贪心
    """

    @override
    def max_non_overlapping(self, nums: list[int], target: int) -> int:
        pre = ans = 0
        cnt = {0}
        for x in nums:
            pre += x
            if pre - target in cnt:
                ans += 1
                cnt = set()
                cnt.clear()
            cnt.add(pre)
        return ans


class SolutionB(Solution):
    """
    前缀和 + 贪心
    使用 python 内置函数 accumulate 代替手动计算前缀和
    """

    @override
    def max_non_overlapping(self, nums: list[int], target: int) -> int:
        ans = 0
        cnt = {0}
        for p in accumulate(nums):
            if p - target in cnt:
                ans += 1
                cnt = set()
            cnt.add(p)
        return ans
