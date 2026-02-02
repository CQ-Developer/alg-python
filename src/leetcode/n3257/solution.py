from abc import ABC, abstractmethod
from typing import override
from math import inf


class Solution(ABC):

    @abstractmethod
    def maximum_value_sum(self, board: list[list[int]]) -> int:
        pass


class SolutionA(Solution):

    @override
    def maximum_value_sum(self, board: list[list[int]]) -> int:
        def update(row: list[int], p: list[tuple[int, int]]):
            for j, x in enumerate(row):
                for k in range(3):
                    if x > p[k][0] and all(j != j2 for _, j2 in p[:k]):
                        p[k], (x, j) = (x, j), p[k]

        m = len(board)
        p, suf = [(-inf, -1)] * 3, [None] * m
        for i in range(m - 1, 1, -1):
            update(board[i], p)
            suf[i] = p[:]

        ans = -inf
        p = [(-inf, -1)] * 3
        for i, row in enumerate(board[:-2]):
            update(row, p)
            for j2, y in enumerate(board[i + 1]):
                for x, j1 in p:
                    for z, j3 in suf[i + 2]:
                        if j1 != j2 and j2 != j3 and j1 != j3:
                            ans = max(ans, x + y + z)
                            break

        return ans
