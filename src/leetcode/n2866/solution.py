from abc import ABC, abstractmethod
from typing import override


class Solution(ABC):

    @abstractmethod
    def maximum_sum_of_heights(self, max_heights: list[int]) -> int:
        pass


class SolutionA(Solution):

    @override
    def maximum_sum_of_heights(self, max_heights: list[int]) -> int:
        n, s = len(max_heights), 0

        stk = [n]
        suf = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            while len(stk) > 1 and max_heights[i] <= max_heights[stk[-1]]:
                j = stk.pop()
                s -= max_heights[j] * (stk[-1] - j)
            s += max_heights[i] * (stk[-1] - i)
            suf[i] = s
            stk.append(i)

        pre = 0
        stk = [-1]
        for i, x in enumerate(max_heights):
            while len(stk) > 1 and x <= max_heights[stk[-1]]:
                j = stk.pop()
                pre -= max_heights[j] * (j - stk[-1])
            pre += x * (i - stk[-1])
            s = max(s, pre + suf[i + 1])
            stk.append(i)

        return s
