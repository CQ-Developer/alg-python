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


class SolutionB(Solution):

    @override
    def maximumSafenessFactor(self, grid: list[list[int]]) -> int:
        n = len(grid)

        # 并查集
        f = list(range(n * n))

        def find(x: int) -> int:
            if f[x] != x:
                f[x] = find(f[x])
            return f[x]

        # 多源BFS
        q: list[tuple[int, int]] = []
        dis = [[-1] * n for _ in range(n)]
        for i, row in enumerate(grid):
            for j, x in enumerate(row):
                if x:
                    q.append((i, j))
                    dis[i][j] = 0
        groups = [q]
        while q:
            tmp = q
            q = []
            for i, j in tmp:
                for x, y in (i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1):
                    if 0 <= x < n and 0 <= y < n and dis[x][y] == -1:
                        q.append((x, y))
                        dis[x][y] = len(groups)
            groups.append(q)
        for g in range(len(groups) - 2, 0, -1):
            for i, j in groups[g]:
                for x, y in (i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1):
                    if 0 <= x < n and 0 <= y < n and dis[x][y] >= dis[i][j]:
                        f[find(x * n + y)] = find(i * n + j)
            if find(0) == find(n * n - 1):
                return g
        return 0
