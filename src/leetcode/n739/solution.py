from abc import ABC, abstractmethod
from typing import override


class Solution(ABC):

    @abstractmethod
    def daily_temperatures(self, temperatures: list[int]) -> list[int]:
        pass


class SolutionA(Solution):

    @override
    def daily_temperatures(self, temperatures: list[int]) -> list[int]:
        n = len(temperatures)
        res = [0] * n
        stk = []
        for i in range(n - 1, -1, -1):
            x = temperatures[i]
            while stk and x >= temperatures[stk[-1]]:
                stk.pop()
            if stk:
                res[i] = stk[-1] - i
            stk.append(i)
        return res
