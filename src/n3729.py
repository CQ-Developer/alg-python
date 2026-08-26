from abc import ABC, abstractmethod
from collections import defaultdict
from typing import override


class Solution(ABC):
    """
    给你一个按非降序排列的整数数组 nums 和一个正整数 k
    如果 nums 的某个子数组的元素和可以被 k 整除, 则称其为良好子数组
    返回一个整数, 表示 nums 中不同的良好子数组的数量

    子数组是数组中连续且非空的一段元素序列

    当两个子数组的数值序列不同, 它们就被视为不同的子数组
    例如, 在 [1,1,1] 中, 有 3 个不同的子数组, 分别是 [1]、[1,1] 和 [1,1,1]
    """

    @abstractmethod
    def num_good_subarrays(self, nums: list[int], k: int) -> int:
        pass


class SolutionA(Solution):
    @override
    def num_good_subarrays(self, nums: list[int], k: int) -> int:
        # 前缀和
        ans = s = 0
        cnt = defaultdict(int)
        for x in nums:
            cnt[s] += 1
            s = (s + x) % k
            ans += cnt[s]
        # 移除重复
        n, i = len(nums), 0
        for j, x in enumerate(nums):
            if j < n - 1 and x == nums[j + 1]:
                continue
            size = j - i + 1
            for sz in range(1, size + 1):
                if x * sz % k == 0:
                    ans -= size - sz
            i = j + 1
        return ans


class SolutionB(Solution):
    @override
    def num_good_subarrays(self, nums: list[int], k: int) -> int:
        cnt = defaultdict(int)
        cnt[0] = 1
        ans = pre = j = 0
        for i, x in enumerate(nums):
            if i and x != nums[i - 1]:
                v = nums[i - 1]
                s = pre
                # 将之前连续相同段的每个前缀和更新到 cnt 中
                for _ in range(i - j):
                    cnt[s % k] += 1
                    s -= v
                j = i
            pre += x
            ans += cnt[pre % k]
        return ans
