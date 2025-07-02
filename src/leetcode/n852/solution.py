from abc import ABC, abstractmethod


class Solution(ABC):

    @abstractmethod
    def peak_index_in_mountain_array(self, arr: list[int]) -> int:
        pass
