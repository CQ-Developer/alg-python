from abc import ABC, abstractmethod


class Solution(ABC):

    @abstractmethod
    def maximumSafenessFactor(self, grid: list[list[int]]) -> int:
        pass
