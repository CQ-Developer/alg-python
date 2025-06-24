from abc import ABC, abstractmethod


class Solution(ABC):

    @abstractmethod
    def median_of_uniqueness_array(self, nums: list[int]) -> int:
        pass
