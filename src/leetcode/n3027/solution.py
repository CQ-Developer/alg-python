from abc import ABC, abstractmethod
from typing import override
from math import inf


class Solution(ABC):

    @abstractmethod
    def number_of_pairs(self, points: list[list[int]]) -> int:
        pass


class SolutionA(Solution):

    @override
    def number_of_pairs(self, points: list[list[int]]) -> int:
        cnt = 0
        points.sort(key=lambda p: (p[0], -p[1]))
        for i, (_, y1) in enumerate(points):
            max_y = -inf
            for _, y2 in points[i + 1 :]:
                if max_y < y2 <= y1:
                    max_y = y2
                    cnt += 1
                if max_y >= y1:
                    break
        return cnt
