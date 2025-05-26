from abc import ABC, abstractmethod


class Solution(ABC):

    @abstractmethod
    def maxDistance(self, position: list[int], m: int) -> int:
        pass
