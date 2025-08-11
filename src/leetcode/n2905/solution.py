from abc import ABC, abstractmethod


class Solution(ABC):

    @abstractmethod
    def find_indices(self, nums: list[int], index_difference: int, value_difference: int) -> list[int]:
        pass
