import abc
import itertools
import math
import typing


class Solution(abc.ABC):
    @abc.abstractmethod
    def min_moves(self, nums: list[int], k: int) -> int:
        pass


class SolutionA(Solution):
    @typing.override
    def min_moves(self, nums: list[int], k: int) -> int:
        p = [q - i for i, q in enumerate(i for i, x in enumerate(nums) if x)]
        s = list(itertools.accumulate(p, initial=0))
        return min(s[i] + s[i + k] - s[i + k // 2] * 2 - p[i + k // 2] * (k & 1) for i in range(len(p) - k + 1))


class SolutionB(Solution):
    @typing.override
    def min_moves(self, nums: list[int], k: int) -> int:
        m = 0
        for i, p in enumerate(i for i, x in enumerate(nums) if x):
            nums[i] = p - i
            m += 1
        if m == len(nums):
            return 0
        ans, p = math.inf, nums
        sl, sm, sr = 0, sum(p[: k // 2]), sum(p[:k])
        for i in range(m - k + 1):
            ans = min(ans, sl + sr - sm * 2 - p[i + k // 2] * (k % 2))
            sl += p[i]
            sm += p[i + k // 2]
            sr += p[i + k]
        return int(ans)
