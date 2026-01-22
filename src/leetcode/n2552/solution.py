from abc import ABC, abstractmethod


class Solution(ABC):

    @abstractmethod
    def count_quadruplets(self, nums: list[int]) -> int:
        pass
