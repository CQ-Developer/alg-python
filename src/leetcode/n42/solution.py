from abc import ABC, abstractmethod
from typing import override
from itertools import accumulate


class Solution(ABC):

    @abstractmethod
    def trap(self, height: list[int]) -> int:
        pass


class SolutionA(Solution):

    @override
    def trap(self, height: list[int]) -> int:
        pre = accumulate(height, max)
        suf = reversed(list(accumulate(reversed(height), max)))
        return sum(min(p, s) - h for p, s, h in zip(pre, suf, height))


class SolutionB(Solution):

    @override
    def trap(self, height: list[int]) -> int:
        ans = 0
        l, r = 0, len(height) - 1
        pre, suf = 0, 0
        while l < r:
            pre = max(pre, height[l])
            suf = max(suf, height[r])
            if pre < suf:
                ans += pre - height[l]
                l += 1
            else:
                ans += suf - height[r]
                r -= 1
        return ans


class SolutionC(Solution):

    @override
    def trap(self, height: list[int]) -> int:
        ans = 0
        stk = []
        for r, x in enumerate(height):
            while stk and height[stk[-1]] <= x:
                h = height[stk.pop()]
                if not stk:
                    break
                l = stk[-1]
                h = min(x, height[l]) - h
                ans += h * (r - l - 1)
            stk.append(r)
        return ans
