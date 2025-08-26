from abc import ABC, abstractmethod
from typing import override


class Solution(ABC):

    @abstractmethod
    def next_greater_element(self, a: list[int], b: list[int]) -> list[int]:
        pass


class SolutionA(Solution):

    @override
    def next_greater_element(self, a: list[int], b: list[int]) -> list[int]:
        stk = [-1]
        idx = dict()
        for x in reversed(b):
            while len(stk) > 1 and x >= stk[-1]:
                stk.pop()
            idx[x] = stk[-1]
            stk.append(x)
        for i, x in enumerate(a):
            a[i] = idx[x]
        return a
