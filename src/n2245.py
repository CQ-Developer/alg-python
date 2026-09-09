from abc import ABC, abstractmethod
from typing import override


class Solution(ABC):
    @abstractmethod
    def max_trailing_zeros(self, grid: list[list[int]]) -> int:
        pass


# 预处理每个数字的因子2和5的数量
c2 = [0] * 1001
c5 = [0] * 1001
for i in range(2, 1001):
    if i % 2 == 0:
        c2[i] = c2[i // 2] + 1
    if i % 5 == 0:
        c5[i] = c5[i // 5] + 1


class SolutionA(Solution):
    @override
    def max_trailing_zeros(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        # 计算每行数字的因子2和5的前缀和
        s = [[(0, 0) for _ in range(n + 1)] for _ in range(m)]
        for i, row in enumerate(grid):
            for j, x in enumerate(row):
                s[i][j + 1] = (s[i][j][0] + c2[x], s[i][j][1] + c5[x])
        ans = 0
        for j, col in enumerate(zip(*grid)):
            # 从上往下, 枚举左拐/右拐
            s2 = s5 = 0
            for i, x in enumerate(col):
                s2 += c2[x]
                s5 += c5[x]
                ans = max(
                    ans,
                    min(s2 + s[i][j][0], s5 + s[i][j][1]),
                    min(s2 + s[i][n][0] - s[i][j + 1][0], s5 + s[i][n][1] - s[i][j + 1][1]),
                )
            # 从下往上, 枚举左拐/右拐
            s2 = s5 = 0
            for i in range(m - 1, -1, -1):
                s2 += c2[col[i]]
                s5 += c5[col[i]]
                ans = max(
                    ans,
                    min(s2 + s[i][j][0], s5 + s[i][j][1]),
                    min(s2 + s[i][n][0] - s[i][j + 1][0], s5 + s[i][n][1] - s[i][j + 1][1]),
                )
        return ans
