from abc import ABC, abstractmethod


class Solution(ABC):

    @abstractmethod
    def pair_sums(self, nums: list[int], target: int) -> list[list[int]]:
        pass
