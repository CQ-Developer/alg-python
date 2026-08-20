from abc import ABC, abstractmethod
from bisect import bisect_left, bisect_right
from itertools import accumulate
from math import inf
from typing import override


class Solution(ABC):
    @abstractmethod
    def min_operations(self, nums: list[int], k: int) -> int:
        pass


class SolutionA(Solution):
    @override
    def min_operations(self, nums: list[int], k: int) -> int:
        ans = inf
        for x in range(k):
            for y in range(k):
                if x != y:
                    s = 0
                    target = (x, y)
                    for i, v in enumerate(nums):
                        d = abs(v % k - target[i & 1])
                        s += min(d, k - d)
                    ans = min(ans, s)
        return int(ans)


class SolutionB(Solution):
    """
    前缀和 + 中位数贪心 + 二分查找
    """

    @override
    def min_operations(self, nums: list[int], k: int) -> int:
        if len(nums) == 1:
            return 0
        a = [[], []]
        for i, x in enumerate(nums):
            a[i & 1].append(x % k)
        min_1x, min_2x, best_x = self.calc(a[0], k)
        min_1y, min_2y, best_y = self.calc(a[1], k)
        if best_x != best_y:
            return min_1x + min_1y
        return min(min_1x + min_2y, min_2x + min_1y)

    def calc(self, a: list[int], k: int) -> tuple[int, int, int]:
        n = len(a)
        a.sort()
        a += [x + k for x in a]
        pre = list(accumulate(a, initial=0))

        def calc_op(target: int) -> int:
            i = bisect_left(a, target, 0, n)
            j = bisect_right(a, target + k // 2, i, i + n)
            s1 = (pre[j] - pre[i]) - (j - i) * target
            s2 = (n + i - j) * (target + k) - (pre[n + i] - pre[j])
            return s1 + s2

        mn1 = mn2 = inf
        best_x = 0
        for x in set(a[:n]):
            op = calc_op(x)
            if op < mn1:
                mn1, mn2 = op, mn1
                best_x = x
            elif op < mn2:
                mn2 = op
        mn2 = min(mn2, calc_op((best_x - 1) % k), calc_op((best_x + 1) % k))
        return int(mn1), int(mn2), best_x
