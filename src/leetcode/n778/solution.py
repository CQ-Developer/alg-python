from abc import ABC, abstractmethod
from typing import override
from collections import deque


class Solution(ABC):

    @abstractmethod
    def swimInWater(self, grid: list[list[int]]) -> int:
        pass


class SolutionA(Solution):

    @override
    def swimInWater(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])

        def check(vis: list[list[bool]], i: int, j: int, mx: int) -> bool:
            if i == m - 1 and j == n - 1:
                return True
            vis[i][j] = True
            if i > 0 and not vis[i - 1][j] and grid[i - 1][j] <= mx and check(vis, i - 1, j, mx):
                return True
            if i + 1 < m and not vis[i + 1][j] and grid[i + 1][j] <= mx and check(vis, i + 1, j, mx):
                return True
            if j > 0 and not vis[i][j - 1] and grid[i][j - 1] <= mx and check(vis, i, j - 1, mx):
                return True
            if j + 1 < n and not vis[i][j + 1] and grid[i][j + 1] <= mx and check(vis, i, j + 1, mx):
                return True
            return False

        l, r = grid[0][0], max(max(g) for g in grid)
        while l < r:
            mid = (l + r) // 2
            if check([[False for _ in range(n)] for _ in range(m)], 0, 0, mid):
                r = mid
            else:
                l = mid + 1
        return r


class SolutionB(Solution):

    @override
    def swimInWater(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])

        def check(mx: int) -> bool:
            q = deque([(0, 0)])
            v = [[False for _ in range(n)] for _ in range(m)]
            v[0][0] = True
            while q:
                i, j = q.popleft()
                for x, y in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
                    if 0 <= x < m and 0 <= y < n and not v[x][y] and grid[x][y] <= mx:
                        v[x][y] = True
                        q.append((x, y))
            return v[m - 1][n - 1]

        l, r = grid[0][0], max(max(g) for g in grid)
        while l < r:
            mid = (l + r) // 2
            if check(mid):
                r = mid
            else:
                l = mid + 1
        return r
