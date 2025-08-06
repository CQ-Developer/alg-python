from abc import ABC, abstractmethod


class Solution(ABC):

    @abstractmethod
    def max_sum(self, nums: list[int]) -> int:
        pass
