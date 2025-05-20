from abc import ABC, abstractmethod
from typing import override


class Solution(ABC):

    @abstractmethod
    def minMaxWeight(self, n: int, edges: list[list[int]], threshold: int) -> int:
        pass


class SolutionA(Solution):

    @override
    def minMaxWeight(self, n: int, edges: list[list[int]], threshold: int) -> int:
        if len(edges) < n - 1:
            return -1
        g: list[list[tuple[int, int]]] = [[] for _ in range(n)]
        for x, y, w in edges:
            g[y].append((x, w))
        vis = [0] * n

        def check(x: int, mx: int) -> int:
            vis[x] = mx
            res = 1
            for y, w in g[x]:
                if w <= mx and vis[y] != mx:
                    res += check(y, mx)
            return res

        w = max(e[2] for e in edges)
        l, r = 1, w + 1
        while l < r:
            m = (l + r) // 2
            if check(0, m) == n:
                r = m
            else:
                l = m + 1
        return -1 if r > w else r
