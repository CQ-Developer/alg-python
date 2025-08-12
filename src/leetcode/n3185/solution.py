from abc import ABC, abstractmethod


class Solution(ABC):

    @abstractmethod
    def count_complete_day_pairs(self, hours: list[int]) -> int:
        pass
