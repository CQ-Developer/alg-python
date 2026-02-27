from abc import ABC, abstractmethod
from typing import override
from itertools import accumulate


class Solution(ABC):

    @abstractmethod
    def longest_WPI(self, hours: list[int]) -> int:
        pass


class SolutionA(Solution):

    @override
    def longest_WPI(self, hours: list[int]) -> int:
        n = len(hours)
        pre = list(accumulate(hours, lambda a, b: a + (1 if b > 8 else -1), initial=0))
        stk = [0]
        for j in range(1, n + 1):
            if pre[j] < pre[stk[-1]]:
                stk.append(j)
        ans = 0
        for i in range(n, 0, -1):
            while stk and pre[i] > pre[stk[-1]]:
                ans = max(ans, i - stk.pop())
        return ans


class SolutionB(Solution):

    @override
    def longest_WPI(self, hours: list[int]) -> int:
        n = len(hours)
        pre = [0] * (n + 1)
        stk = [0]
        for j in range(1, n + 1):
            pre[j] = pre[j - 1] + (1 if hours[j - 1] > 8 else -1)
            if pre[j] < pre[stk[-1]]:
                stk.append(j)
        ans = 0
        for i in range(n, 0, -1):
            while stk and pre[i] > pre[stk[-1]]:
                ans = max(ans, i - stk.pop())
        return ans


class SolutionC(Solution):

    @override
    def longest_WPI(self, hours: list[int]) -> int:
        h = {0: -1}
        p = a = 0
        for i, x in enumerate(hours):
            p += 1 if x > 8 else -1
            if p > 0:
                a = i + 1
            else:
                if p - 1 in h:
                    a = max(a, i - h[p - 1])
                if p not in h:
                    h[p] = i
        return a


class SolutionD(Solution):

    @override
    def longest_WPI(self, hours: list[int]) -> int:
        n = len(hours)
        pos = [0] * (n + 2)
        a = p = 0
        for i, h in enumerate(hours, start=1):
            p -= 1 if h > 8 else -1
            if p < 0:
                a = i
            else:
                if pos[p + 1]:
                    a = max(a, i - pos[p + 1])
                if pos[p] == 0:
                    pos[p] = i
        return a
