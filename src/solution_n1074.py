from abc import ABC, abstractmethod
from collections import defaultdict
from typing import override


class Solution(ABC):
    @abstractmethod
    def num_submatrix_sum_target(self, matrix: list[list[int]], target: int) -> int:
        pass


class SolutionA(Solution):
    @override
    def num_submatrix_sum_target(self, matrix: list[list[int]], target: int) -> int:
        n = len(matrix[0])
        ans = 0
        for i in range(len(matrix)):
            pre = [0] * n
            for row in matrix[i:]:
                for j, x in enumerate(row):
                    pre[j] += x
                cnt = defaultdict(int)
                s = 0
                for j, x in enumerate(pre):
                    cnt[s] += 1
                    s += x
                    ans += cnt[s - target]
        return ans
