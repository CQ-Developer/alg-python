from abc import ABC, abstractmethod


class Solution(ABC):

    @abstractmethod
    def swinInWater(self, grid: list[list[int]]) -> int:
        pass
