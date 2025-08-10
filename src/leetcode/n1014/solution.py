from abc import ABC, abstractmethod


class Solution(ABC):

    @abstractmethod
    def max_score_sightseeing_pair(self, values: list[int]) -> int:
        pass
