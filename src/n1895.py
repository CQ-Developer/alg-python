import abc
import typing


class Solution(abc.ABC):
    @abc.abstractmethod
    def largest_magic_square(self, grid: list[list[int]]) -> int:
        pass


class SolutionA(Solution):
    @typing.override
    def largest_magic_square(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])

        row_sum = [[0] * (n + 1) for _ in range(m)]
        col_sum = [[0] * n for _ in range(m + 1)]
        diag_sum = [[0] * (n + 1) for _ in range(m + 1)]
        anti_sum = [[0] * (n + 1) for _ in range(m + 1)]
        for i, row in enumerate(grid):
            for j, x in enumerate(row):
                row_sum[i][j + 1] = row_sum[i][j] + x
                col_sum[i + 1][j] = col_sum[i][j] + x
                diag_sum[i + 1][j + 1] = diag_sum[i][j] + x
                anti_sum[i + 1][j] = anti_sum[i][j + 1] + x

        for k in range(min(m, n), 1, -1):
            for i in range(k, m + 1):
                for j in range(k, n + 1):
                    s = diag_sum[i][j] - diag_sum[i - k][j - k]
                    if (
                        anti_sum[i][j - k] - anti_sum[i - k][j] == s
                        and all(row_sum[r][j] - row_sum[r][j - k] == s for r in range(i - k, i))
                        and all(col_sum[i][c] - col_sum[i - k][c] == s for c in range(j - k, j))
                    ):
                        return k

        return 1
