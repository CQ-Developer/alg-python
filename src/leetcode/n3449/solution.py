from abc import ABC, abstractmethod


class Solution(ABC):

    @abstractmethod
    def maxScore(self, points: list[int], m: int) -> int:
        pass
