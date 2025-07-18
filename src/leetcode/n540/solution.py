from abc import ABC, abstractmethod


class Solution(ABC):

    @abstractmethod
    def single_non_duplicate(self, nums: list[int]) -> int:
        pass
