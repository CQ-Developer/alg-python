from abc import ABC, abstractmethod


class Solution(ABC):

    @abstractmethod
    def maximum_product(self, nums: list[int], m: int) -> int:
        pass
