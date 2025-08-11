from abc import ABC, abstractmethod


class Solution(ABC):

    @abstractmethod
    def num_pairs_divisible_by_60(self, time: list[int]) -> int:
        pass
