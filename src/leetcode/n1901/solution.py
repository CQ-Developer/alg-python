from abc import ABC, abstractmethod


class Solution(ABC):

    @abstractmethod
    def find_peak_grid(self, mat: list[list[int]]) -> list[int]:
        pass
