from abc import ABC, abstractmethod


class Solution(ABC):

    @abstractmethod
    def maxPossibleScore(self, start: list[int], d: int) -> int:
        pass
