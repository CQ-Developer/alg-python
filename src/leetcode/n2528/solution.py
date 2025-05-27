from abc import ABC, abstractmethod


class Solution(ABC):

    @abstractmethod
    def maxPower(self, stations: list[int], r: int, k: int) -> int:
        pass
