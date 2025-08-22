from abc import ABC, abstractmethod
from typing import override


class Solution(ABC):

    @abstractmethod
    def cal_points(self, operations: list[str]) -> int:
        pass


class SolutionA(Solution):

    @override
    def cal_points(self, operations: list[str]) -> int:
        a = []
        for o in operations:
            if o == 'C':
                a.pop()
            elif o == 'D':
                a.append(a[-1] * 2)
            elif o == '+':
                a.append(a[-2] + a[-1])
            else:
                a.append(int(o))
        return sum(a)


class SolutionB(Solution):

    @override
    def cal_points(self, operations: list[str]) -> int:
        i = 0
        a = [0] * len(operations)
        for s in operations:
            if s == 'C':
                a[i - 1] = 0
                i -= 1
            elif s == 'D':
                a[i] = a[i - 1] * 2
                i += 1
            elif s == '+':
                a[i] = a[i - 1] + a[i - 2]
                i += 1
            else:
                a[i] = int(s)
                i += 1
        return sum(a)
