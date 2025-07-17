from abc import ABC, abstractmethod


class Solution(ABC):

    @abstractmethod
    def find_kth_positive(self, arr: list[int], k: int) -> int:
        pass
