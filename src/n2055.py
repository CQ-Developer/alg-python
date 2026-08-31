import abc
import itertools
import typing


class Solution(abc.ABC):
    @abc.abstractmethod
    def plates_between_candles(self, s: str, queries: list[list[int]]) -> list[int]:
        pass


class SolutionA(Solution):
    @typing.override
    def plates_between_candles(self, s: str, queries: list[list[int]]) -> list[int]:
        n = len(s)

        # left[i] 表示 i 左侧最近的蜡烛
        left = [0] * n
        p = -1
        for i, x in enumerate(s):
            if x == "|":
                p = i
            left[i] = p

        # right[i] 表示 i 右侧最近的蜡烛
        right = [0] * n
        p = n
        for i in range(n - 1, -1, -1):
            if s[i] == "|":
                p = i
            right[i] = p

        # 前缀和
        pre = list(itertools.accumulate(s, lambda acc, c: acc + (c == "*"), initial=0))

        n = len(queries)
        ans = [0] * n
        for i, (l, r) in enumerate(queries):
            l, r = right[l], left[r]
            if l < r:
                ans[i] = pre[r] - pre[l]
        return ans
