from abc import ABC, abstractmethod
from collections import defaultdict
from typing import override

from sortedcontainers import SortedList


class Solution(ABC):
    """
    给你一个整数数组 nums 和一个整数 target
    返回数组 nums 中满足 target 是主要元素的子数组数目
    一个子数组的主要元素是指该元素在该子数组中出现的次数严格大于其长度的一半
    子数组是数组中一段连续且非空的元素序列
    """

    @abstractmethod
    def count_majority_subarrays(self, nums: list[int], target: int) -> int:
        pass


class SolutionA(Solution):
    """
    前缀和 + 有序集合
    """

    @override
    def count_majority_subarrays(self, nums: list[int], target: int) -> int:
        sl = SortedList([0])
        ans = s = 0
        for x in nums:
            s += 1 if x == target else -1
            ans += sl.bisect_left(s)
            sl.add(s)
        return ans


class SolutionB(Solution):
    """
    前缀和 + 动态规划
    f[j] = f[j - 1] + cnt[p[j - 1]]
    f[j] = f[j - 1] - cnt[p[j]]
    """

    def count_majority_subarrays(self, nums: list[int], target: int) -> int:
        cnt = defaultdict(int)
        cnt[0] = 1
        ans = p = f = 0
        for x in nums:
            if x == target:
                f += cnt[p]
                p += 1
            else:
                p -= 1
                f -= cnt[p]
            ans += f
            cnt[p] += 1
        return ans
