from abc import ABC, abstractmethod


class Solution(ABC):

    @abstractmethod
    def minMaxWeight(self, n: int, edges: list[list[int]], threshold: int) -> int:
        pass
