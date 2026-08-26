from abc import ABC, abstractmethod
from itertools import accumulate
from typing import override


class Solution(ABC):
    @abstractmethod
    def count_valid_subarrays(self, nums: list[int], x: int) -> int:
        pass


class SolutionA(Solution):
    """
    暴力
    """

    @override
    def count_valid_subarrays(self, nums: list[int], x: int) -> int:
        a, n = 0, len(nums)
        # 枚举子数组的起始位置
        for i in range(n):
            s = 0
            # 枚举每个子数组和
            for v in nums[i:]:
                s += v
                # 判断最低位是否为x
                if s % 10 != x:
                    continue
                # 判断最高位是否为x
                t = s
                while t > 9:
                    t //= 10
                if t == x:
                    a += 1
        return a


class SolutionB(Solution):
    @override
    def count_valid_subarrays(self, nums: list[int], x: int) -> int:
        ans = 0
        pre = list(accumulate(nums, initial=0))
        low, high = x, x + 1
        while low <= pre[-1]:
            a = b = 0
            cnt = [0] * 10
            for s in pre:
                # s - pre[a] >= high 离开区间
                while s - pre[a] >= high:
                    cnt[pre[a] % 10] -= 1
                    a += 1
                # s - pre[b] >= low 进入区间
                while s - pre[b] >= low:
                    cnt[pre[b] % 10] += 1
                    b += 1
                ans += cnt[(s - x) % 10]
            low *= 10
            high *= 10
        return ans
