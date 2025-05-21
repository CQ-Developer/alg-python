from abc import ABC, abstractmethod


class Solution(ABC):

    @abstractmethod
    def minTime(self, time: list[int], m: int) -> int:
        pass
