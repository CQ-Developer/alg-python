from abc import ABC, abstractmethod


class Solution(ABC):

    @abstractmethod
    def range_sum(self, nums: list[int], n: int, left: int, right: int) -> int:
        pass
