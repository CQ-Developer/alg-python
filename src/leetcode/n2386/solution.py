from abc import ABC, abstractmethod


class Solution(ABC):

    @abstractmethod
    def k_sum(self, nums: list[int], k: int) -> int:
        pass
