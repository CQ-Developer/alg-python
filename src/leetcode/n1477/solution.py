from abc import ABC, abstractmethod
from typing import override
from itertools import accumulate


class Solution(ABC):

    @abstractmethod
    def min_sum_of_lengths(self, arr: list[int], target: int) -> int:
        pass


class SolutionA(Solution):
    """
    前缀和
    """

    @override
    def min_sum_of_lengths(self, arr: list[int], target: int) -> int:
        n = len(arr)
        p, ans = 0, n + 1
        cnt = {0: -1}
        f = [n] * (n + 1)
        for i, x in enumerate(arr):
            p += x
            if p - target in cnt:
                j = cnt[p - target]
                ans = min(ans, i - j + f[j + 1])
                f[i + 1] = min(f[i], i - j)
            else:
                f[i + 1] = f[i]
            cnt[p] = i
        return -1 if ans == n + 1 else ans


class SolutionB(Solution):
    """
    滑窗
    """

    @override
    def min_sum_of_lengths(self, arr: list[int], target: int) -> int:
        n = len(arr)
        ans = n + 1
        f = [n] * (n + 1)
        l = r = s = 0
        while r < n:
            s += arr[r]
            while s > target:
                s -= arr[l]
                l += 1
            if s == target:
                ans = min(ans, r - l + 1 + f[l])
                f[r + 1] = min(f[r], r - l + 1)
            else:
                f[r + 1] = f[r]
            r += 1
        return -1 if ans == n + 1 else ans
