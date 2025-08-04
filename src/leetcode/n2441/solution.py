from abc import ABC, abstractmethod


class Solution(ABC):

    @abstractmethod
    def find_max_k(self, nums: list[int]) -> int:
        pass
