from abc import ABC, abstractmethod


class Solution(ABC):

    @abstractmethod
    def find_kth_smallest(self, coins: list[int], k: int) -> int:
        pass
