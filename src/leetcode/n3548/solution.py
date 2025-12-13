from abc import ABC, abstractmethod
from typing import override, Sequence


class Solution(ABC):

    @abstractmethod
    def can_partition_grid(self, grid: list[list[int]]) -> bool:
        pass


class SolutionA(Solution):

    @override
    def can_partition_grid(self, grid: list[list[int]]) -> bool:
        total = sum(sum(row) for row in grid)

        def check(g: Sequence[Sequence[int]]) -> bool:
            n = len(g[0])

            def do_cnt(g: Sequence[Sequence[int]]) -> bool:
                s = 0
                st = {0}
                for i, row in enumerate(g[:-1]):
                    for j, x in enumerate(row):
                        s += x
                        if i > 0 or j == 0 or j == n - 1:
                            st.add(x)
                    if n == 1:
                        if s * 2 == total or s * 2 - total == g[0][0] or s * 2 - total == row[0]:
                            return True
                        continue
                    if s * 2 - total in st:
                        return True
                    if i == 0:
                        st.update(row)
                return False

            return do_cnt(g) or do_cnt(g[::-1])

        return check(grid) or check(list(zip(*grid)))
