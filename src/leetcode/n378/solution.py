from abc import ABC, abstractmethod


class Solution(ABC):

    @abstractmethod
    def kthSmallest(self, matrix: list[list[int]], k: int) -> int:
        pass
