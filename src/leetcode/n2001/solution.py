from abc import ABC, abstractmethod


class Solution(ABC):

    @abstractmethod
    def interchangeable_rectangles(self, rectangles: list[list[int]]) -> int:
        pass
