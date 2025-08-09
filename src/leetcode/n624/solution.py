from abc import ABC, abstractmethod


class Solution(ABC):

    @abstractmethod
    def max_distance(self, arrays: list[list[int]]) -> int:
        pass
