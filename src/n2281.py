from abc import ABC, abstractmethod
from itertools import accumulate
from typing import override


class Solution(ABC):
    @abstractmethod
    def total_strength(self, strength: list[int]) -> int:
        pass


class SolutionA(Solution):
    @override
    def total_strength(self, strength: list[int]) -> int:
        # 当前数字作为最小值的左右边界
        n = len(strength)
        left, right = [-1] * n, [n] * n
        stk = []
        for i, x in enumerate(strength):
            while stk and x <= strength[stk[-1]]:
                right[stk.pop()] = i
            if stk:
                left[i] = stk[-1]
            stk.append(i)
        # 二重前缀和
        ans = 0
        ss = list(accumulate(accumulate(strength, initial=0), initial=0))
        for i, x in enumerate(strength):
            l, r = left[i] + 1, right[i] - 1
            total = (i + 1 - l) * (ss[r + 2] - ss[i + 1]) - (r + 1 - i) * (ss[i + 1] - ss[l])
            ans += total * x
        return ans % 1000000007
