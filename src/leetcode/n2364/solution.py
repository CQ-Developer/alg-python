from abc import ABC, abstractmethod


class Solution(ABC):

    @abstractmethod
    def count_bad_pairs(self, nums: list[int]) -> int:
        pass
