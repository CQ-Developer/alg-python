from abc import ABC, abstractmethod
from typing import override
from collections import deque


class Solution(ABC):

    @abstractmethod
    def maximumSafenessFactor(self, grid: list[list[int]]) -> int:
        pass


class SolutionA(Solution):

    @override
    def maximumSafenessFactor(self, grid: list[list[int]]) -> int:
        n = len(grid)
        dis = [[-1 for _ in range(n)] for _ in range(n)]

        def check(m: int) -> bool:
            que = deque([(0, 0)])
            vis = set([(0, 0)])
            while que:
                i, j = que.popleft()
                for x, y in (i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1):
                    if 0 <= x < n and 0 <= y < n and (x, y) not in vis and dis[x][y] >= m:
                        vis.add((x, y))
                        que.append((x, y))
            return (n - 1, n - 1) in vis

        que: deque[tuple[int, int]] = deque()
        for i, row in enumerate(grid):
            for j, x in enumerate(row):
                if x == 1:
                    que.append((i, j))
                    dis[i][j] = 0
        while que:
            i, j = que.popleft()
            for x, y in (i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1):
                if 0 <= x < n and 0 <= y < n and dis[x][y] == -1:
                    dis[x][y] = dis[i][j] + 1
                    que.append((x, y))
        l, r = 0, min(dis[0][0], dis[-1][-1])
        while l <= r:
            m = (l + r) // 2
            if check(m):
                l = m + 1
            else:
                r = m - 1
        return r
