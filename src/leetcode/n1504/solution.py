from abc import ABC, abstractmethod
from typing import override


class Solution(ABC):

    @abstractmethod
    def num_submat(self, mat: list[list[int]]) -> int:
        pass


class SolutionA(Solution):

    @override
    def num_submat(self, mat: list[list[int]]) -> int:
        n = len(mat[0])
        ans = 0
        height = [0] * n
        for row in mat:
            for j, x in enumerate(row):
                if x == 1:
                    height[j] += 1
                else:
                    height[j] = 0
            stk = [(-1, 0, -1)]
            for r, h in enumerate(height):
                while stk and stk[-1][2] >= h:
                    stk.pop()
                l, f, _ = stk[-1]
                f += h * (r - l)
                ans += f
                stk.append((r, f, h))
        return ans
