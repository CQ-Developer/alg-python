from abc import ABC, abstractmethod
from collections import defaultdict
from itertools import accumulate
from typing import override


class Solution(ABC):
    """
    给你一个下标从 0 开始的整数数组 nums

    现有一个长度等于 nums.length 的数组 arr.
    对于满足 nums[j] == nums[i] 且 j != i 的所有 j,
    arr[i] 等于所有 |i - j| 之和.
    如果不存在这样的 j, 则令 arr[i] 等于 0.

    返回数组 arr.

    1 <= nums.length <= 10^5
    0 <= nums[i] <= 10^9
    """

    @abstractmethod
    def distance(self, nums: list[int]) -> list[int]:
        pass


class SolutionA(Solution):
    """
    暴力 (超时)
    """

    @override
    def distance(self, nums: list[int]) -> list[int]:
        n = len(nums)
        arr = [0] * n
        for i, x in enumerate(nums):
            for j, y in enumerate(nums):
                if j != i and x == y:
                    arr[i] += abs(i - j)
        return arr


class SolutionB(Solution):
    """
    前缀和 + 分组循环
    """

    @override
    def distance(self, nums: list[int]) -> list[int]:
        groups = defaultdict(list)
        for i, x in enumerate(nums):
            groups[x].append(i)
        ans = [0] * len(nums)
        for a in groups.values():
            n = len(a)
            s = list(accumulate(a, initial=0))
            for j, x in enumerate(a):
                left = x * j - s[j]
                right = s[n] - s[j] - x * (n - j)
                ans[x] = left + right
        return ans
