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


class SolutionB(Solution):

    @override
    def num_submat(self, mat: list[list[int]]) -> int:
        ans = 0
        m, n = len(mat), len(mat[0])
        for t in range(m):
            a = [0] * n
            for i in range(t, m):
                h = i - t + 1
                p = -1
                for j in range(n):
                    a[j] += mat[i][j]
                    if a[j] == h:
                        ans += j - p
                    else:
                        p = j
        return ans
