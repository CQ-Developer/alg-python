from abc import ABC, abstractmethod


class Solution(ABC):

    @abstractmethod
    def num_identical_pairs(self, nums: list[int]) -> int:
        pass
