from abc import ABC, abstractmethod


class Solution(ABC):

    @abstractmethod
    def find_min(self, nums: list[int]) -> int:
        pass
