from abc import ABC, abstractmethod


class Solution(ABC):

    @abstractmethod
    def maxDistance(self, side: int, points: list[list[int]], k: int) -> int:
        pass
