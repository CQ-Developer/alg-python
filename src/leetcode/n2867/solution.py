from abc import ABC, abstractmethod
from typing import override
from math import isqrt

N = 10**5 + 1
is_prime = [True] * N
is_prime[1] = False
for i in range(2, isqrt(N) + 1):
    if is_prime[i]:
        for j in range(i * i, N, i):
            is_prime[j] = False


class Solution(ABC):

    @abstractmethod
    def count_paths(self, n: int, edges: list[list[int]]) -> int:
        pass


class SolutionA(Solution):

    @override
    def count_paths(self, n: int, edges: list[list[int]]) -> int:
        g = [[] for _ in range(n + 1)]
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)

        def dfs(nodes: list[int], x: int, f: int):
            nodes.append(x)
            for y in g[x]:
                if y != f and not is_prime[y]:
                    dfs(nodes, y, x)

        ans = 0
        size = [0] * (n + 1)
        for x in range(2, n + 1):
            if is_prime[x]:
                s = 0
                for y in g[x]:
                    if is_prime[y]:
                        continue
                    if size[y] == 0:
                        nodes = []
                        dfs(nodes, y, x)
                        for z in nodes:
                            size[z] = len(nodes)
                    ans += size[y] * s
                    s += size[y]
                ans += s

        return ans
