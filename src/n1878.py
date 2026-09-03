import abc
import typing


class Solution(abc.ABC):
    @abc.abstractmethod
    def get_biggest_three(self, grid: list[list[int]]) -> list[int]:
        pass


class SolutionA(Solution):
    """
    前缀和
    """

    @typing.override
    def get_biggest_three(self, grid: list[list[int]]) -> list[int]:
        m, n = len(grid), len(grid[0])
        # ↘ 方向的前缀和
        diag_sum = [[0] * (n + 1) for _ in range(m + 1)]
        # ↙ 方向的前缀和
        anti_sum = [[0] * (n + 1) for _ in range(m + 1)]
        for i, row in enumerate(grid):
            for j, v in enumerate(row):
                diag_sum[i + 1][j + 1] = diag_sum[i][j] + v
                anti_sum[i + 1][j] = anti_sum[i][j + 1] + v

        # 从 (x,y) ↘ 连续 k 个数的和
        def query_diag(x: int, y: int, k: int) -> int:
            return diag_sum[x + k][y + k] - diag_sum[x][y]

        # 从 (x,y) ↙ 连续 k 个数的和
        def query_anti(x: int, y: int, k: int) -> int:
            return anti_sum[x + k][y + 1 - k] - anti_sum[x][y + 1]

        x = y = z = 0

        # 更新最大/次大/第三大
        def update(v: int):
            nonlocal x, y, z
            if x < v:
                x, y, z = v, x, y
            elif y < v < x:
                y, z = v, y
            elif z < v < y:
                z = v

        for i, row in enumerate(grid):
            for j, v in enumerate(row):
                update(v)
                mx = min(i, m - 1 - i, j, n - 1 - j)
                for k in range(1, mx + 1):
                    # 右上边
                    a = query_diag(i - k, j, k)
                    # 左下边
                    b = query_diag(i, j - k, k)
                    # 左上边
                    c = query_anti(i - k + 1, j - 1, k - 1)
                    # 右下边
                    d = query_anti(i, j + k, k + 1)
                    update(a + b + c + d)

        ans = [x, y, z]
        while ans[-1] == 0:
            ans.pop()
        return ans
