from abc import ABC, abstractmethod


class Solution(ABC):

    @abstractmethod
    def get_largest_outlier(self, nums: list[int]) -> int:
        pass
