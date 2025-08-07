from abc import ABC, abstractmethod


class Solution(ABC):

    @abstractmethod
    def max_operations(self, nums: list[int], k: int) -> int:
        pass
