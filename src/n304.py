from abc import ABC, abstractmethod
from typing import override


class NumMatrix(ABC):
    def __init__(self, matrix: list[list[int]]):
        pass

    @abstractmethod
    def sum_region(self, row1: int, col1: int, row2: int, col2: int) -> int:
        pass


class NumMatrixA(NumMatrix):
    """
    暴力解
    """

    def __init__(self, matrix: list[list[int]]):
        self.matrix = matrix

    @override
    def sum_region(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return sum(self.matrix[i][j] for i in range(row1, row2 + 1) for j in range(col1, col2 + 1))


class NumMatrixB(NumMatrix):
    """
    二维前缀和
    """

    def __init__(self, matrix: list[list[int]]):
        m, n = len(matrix), len(matrix[0])
        s = [[0] * (n + 1) for _ in range(m + 1)]
        for i, row in enumerate(matrix):
            for j, x in enumerate(row):
                s[i + 1][j + 1] = s[i + 1][j] + s[i][j + 1] - s[i][j] + x
        self.s = s

    @override
    def sum_region(self, row1: int, col1: int, row2: int, col2: int) -> int:
        s = self.s
        return s[row2 + 1][col2 + 1] - s[row2 + 1][col1] - s[row1][col2 + 1] + s[row1][col1]
