from abc import ABC, abstractmethod
from itertools import accumulate
from math import inf
from typing import override

from sortedcontainers import SortedList


class Solution(ABC):
    @abstractmethod
    def minimum_sum_subarray(self, nums: list[int], l: int, r: int) -> int:
        pass


class SolutionA(Solution):
    """
    暴力
    """

    @override
    def minimum_sum_subarray(self, nums: list[int], l: int, r: int) -> int:
        n = len(nums)
        ans = inf
        for i in range(n - l + 1):
            s = 0
            for j in range(i, min(n, i + r)):
                s += nums[j]
                if s > 0 and j - i + 1 >= l:
                    ans = min(ans, s)
        return -1 if ans == inf else int(ans)


class SolutionB(Solution):
    """
    前缀和 + 有序集合

    设前缀和数组为 s, 则子数组 [i, j) 的和为 s[j] - s[i]

    根据题目要求进行变换:
    - s[j] - s[i] > 0
    - l <= j - i <= r

    当我们遍历右侧 j 时, 需要找满足如下的条件的 i
    - s[i] < s[j]
    - j - r <= i <= j - l

    由于题目要求找到符合上述条件的子数组和的最小值
    所以找小于 s[j] 的最大值同时维护 i 的合理范围即可
    """

    @override
    def minimum_sum_subarray(self, nums: list[int], l: int, r: int) -> int:
        ans = inf
        s = list(accumulate(nums, initial=0))
        sl = SortedList()
        for j in range(l, len(s)):
            sl.add(s[j - l])
            k = sl.bisect_left(s[j])
            if k:
                ans = min(ans, s[j] - sl[k - 1])
            if j >= r:
                sl.remove(s[j - r])
        return -1 if ans == inf else int(ans)
