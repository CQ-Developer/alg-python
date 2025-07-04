from abc import ABC, abstractmethod


class Solution(ABC):

    @abstractmethod
    def search(self, nums: list[int], target: int) -> int:
        pass
