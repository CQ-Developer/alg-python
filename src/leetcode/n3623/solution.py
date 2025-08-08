from abc import ABC, abstractmethod


class Solution(ABC):

    @abstractmethod
    def count_trapezoids(self, points: list[list[int]]) -> int:
        pass
