from abc import ABC, abstractmethod


class Solution(ABC):

    @abstractmethod
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        pass
