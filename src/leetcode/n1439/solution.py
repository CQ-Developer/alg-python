from abc import ABC, abstractmethod


class Solution(ABC):

    @abstractmethod
    def kth_smallest(self, mat: list[list[int]], k: int) -> int:
        pass
