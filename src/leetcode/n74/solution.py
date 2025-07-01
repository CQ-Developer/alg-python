from abc import ABC, abstractmethod


class Solution(ABC):

    @abstractmethod
    def search_matrix(self, matrix: list[list[int]], target: int) -> bool:
        pass
