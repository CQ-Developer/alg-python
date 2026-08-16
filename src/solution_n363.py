from abc import ABC, abstractmethod
from math import inf
from typing import override

from sortedcontainers import SortedList


class Solution(ABC):
    """
    给你一个 m * n 的矩阵 matrix 和一个整数 k,
    找出并返回矩阵内部矩形区域的不超过 k 的最大数值和

    题目数据保证会存在一个数值和不超过 k 的矩形区域

    参数:
    m == matrix.length
    n == matrix[i].length
    1 <= m, n <= 100
    -100 <= matrix[i][j] <= 100
    -10^5 <= k <= 10^5
    """

    @abstractmethod
    def max_sum_submatrix(self, matrix: list[list[int]], k: int) -> int:
        pass


class SolutionA(Solution):
    """
    1. 将二维问题转换成一维问题
    """

    @override
    def max_sum_submatrix(self, matrix: list[list[int]], k: int) -> int:
        ans = -inf
        m, n = len(matrix), len(matrix[0])
        # 枚举上界
        for i in range(m):
            s = [0] * n
            # 枚举下界
            for j in range(i, m):
                # 计算列的累加
                for c, x in enumerate(matrix[j]):
                    s[c] += x
                # 前缀和
                p = 0
                cnt = SortedList([0])
                for v in s:
                    p += v
                    pos = cnt.bisect_left(p - k)
                    if pos < len(cnt):
                        ans = max(ans, p - cnt[pos])
                    cnt.add(p)
        return int(ans)
