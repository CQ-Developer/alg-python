from abc import ABC, abstractmethod


class Solution(ABC):

    @abstractmethod
    def contains_nearby_duplicate(self, nums: list[int], k: int) -> bool:
        pass
