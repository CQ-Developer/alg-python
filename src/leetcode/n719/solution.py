from abc import ABC, abstractmethod


class Solution(ABC):

    @abstractmethod
    def smallestDistancePair(self, nums: list[int], k: int) -> int:
        pass
