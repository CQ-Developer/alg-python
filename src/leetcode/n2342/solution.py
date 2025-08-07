from abc import ABC, abstractmethod


class Solution(ABC):

    @abstractmethod
    def maximum_sum(self, nums: list[int]) -> int:
        pass
