import abc
import collections
import typing


class Solution(abc.ABC):
    @abc.abstractmethod
    def count_palindrome_paths(self, parent: list[int], s: str) -> int:
        pass


class SolutionA(Solution):
    @typing.override
    def count_palindrome_paths(self, parent: list[int], s: str) -> int:
        n = len(parent)

        g = [[] for _ in range(n)]
        for i in range(1, n):
            g[parent[i]].append(i)

        cnt = collections.Counter([0])

        def dfs(v: int, xor: int) -> int:
            res = 0
            for w in g[v]:
                bit = 1 << (ord(s[w]) - 97)
                x = xor ^ bit
                res += cnt[x] + sum(cnt[x ^ (1 << i)] for i in range(26))
                cnt[x] += 1
                res += dfs(w, x)
            return res

        return dfs(0, 0)
