from abc import ABC, abstractmethod
from typing import override
from math import inf


class Solution(ABC):

    @abstractmethod
    def car_fleet(self, target: int, position: list[int], speed: list[int]) -> int:
        pass


class SolutionA(Solution):

    @override
    def car_fleet(self, target: int, position: list[int], speed: list[int]) -> int:
        stk = [inf]
        for p, s in sorted(zip(position, speed)):
            t = (target - p) / s
            while t >= stk[-1]:
                stk.pop()
            stk.append(t)
        return len(stk) - 1


class SolutionB(Solution):

    @override
    def car_fleet(self, target: int, position: list[int], speed: list[int]) -> int:
        pre = cnt = 0
        for p, s in sorted(zip(position, speed), reverse=True):
            t = (target - p) / s
            if t > pre:
                cnt += 1
                pre = t
        return cnt
