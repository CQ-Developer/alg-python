from abc import ABC, abstractmethod
from bisect import bisect_left
from typing import override


class Solution(ABC):
    @abstractmethod
    def minimum_cost(self, nums: list[int]) -> int:
        pass


# 生成有序回文数
pal = []
base = 1
while base <= 10000:
    # 奇数长度
    for i in range(base, base * 10):
        x = i
        t = i // 10
        while t:
            x = x * 10 + t % 10
            t //= 10
        pal.append(x)
    # 偶数长度
    if base <= 1000:
        for i in range(base, base * 10):
            x = t = i
            while t:
                x = x * 10 + t % 10
                t //= 10
            pal.append(x)
    base *= 10
pal.append(1_000_000_001)


class SolutionA(Solution):
    @override
    def minimum_cost(self, nums: list[int]) -> int:
        n = len(nums)

        nums.sort()
        i = bisect_left(pal, nums[(n - 1) // 2])

        # nums[(n - 1) // 2] <= pal[i] <= nums[n // 2]
        if pal[i] <= nums[n // 2]:
            return sum(abs(x - pal[i]) for x in nums)

        # 距离中位数最近的2个回文数 pal[i] 和 pal[i - 1]
        return min(
            sum(abs(x - pal[i]) for x in nums),
            sum(abs(x - pal[i - 1]) for x in nums),
        )
