from abc import ABC, abstractmethod
from typing import override
from itertools import accumulate


class Solution(ABC):

    @abstractmethod
    def total_strength(self, strength: list[int]) -> int:
        pass


class SolutionA(Solution):

    @override
    def total_strength(self, strength: list[int]) -> int:
        n = len(strength)

        stk = []
        left, right = [-1] * n, [n] * n
        for i, x in enumerate(strength):
            while stk and strength[stk[-1]] >= x:
                right[stk.pop()] = i
            if stk:
                left[i] = stk[-1]
            stk.append(i)

        ss = list(accumulate(accumulate(strength, initial=0), initial=0))

        ans = 0
        for i, x in enumerate(strength):
            l, r = left[i] + 1, right[i] - 1
            total = (i - l + 1) * (ss[r + 2] - ss[i + 1]) - (r - i + 1) * (ss[i + 1] - ss[l])
            ans += x * total
        return ans % 1_000_000_007
