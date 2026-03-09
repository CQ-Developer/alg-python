from abc import ABC, abstractmethod
from typing import override
from collections import defaultdict


class Solution(ABC):

    @abstractmethod
    def num_submatrix_sum_target(self, matrix: list[list[int]], target: int) -> int:
        pass


class SolutionA(Solution):

    @override
    def num_submatrix_sum_target(self, matrix: list[list[int]], target: int) -> int:
        m, n = len(matrix), len(matrix[0])
        ans = 0
        for i in range(m):
            p = [0] * n
            for row in matrix[i:]:
                for j, x in enumerate(row):
                    p[j] += x
                cnt = defaultdict(int)
                s = 0
                for j, x in enumerate(p):
                    cnt[s] += 1
                    s += x
                    ans += cnt[s - target]
        return ans
