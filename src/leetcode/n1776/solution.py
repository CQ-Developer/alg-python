from abc import ABC, abstractmethod
from typing import override


class Solution(ABC):

    @abstractmethod
    def get_collision_times(self, cars: list[list[int]]) -> list[float]:
        pass


class SolutionA(Solution):

    @override
    def get_collision_times(self, cars: list[list[int]]) -> list[float]:
        n = len(cars)
        ans = [-1.0] * n
        stk = [n - 1]
        for i in range(n - 2, -1, -1):
            i_pos, i_spd = cars[i]
            while stk:
                j = stk[-1]
                j_pos, j_spd = cars[j]
                if i_spd <= j_spd:
                    stk.pop()
                else:
                    cst = (j_pos - i_pos) / (i_spd - j_spd)
                    if ans[j] != -1 and cst >= ans[j]:
                        stk.pop()
                    else:
                        ans[i] = cst
                        break
            stk.append(i)
        return ans
