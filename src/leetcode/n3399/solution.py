from abc import ABC, abstractmethod


class Solution(ABC):

    @abstractmethod
    def minLength(self, s: str, numOps: int) -> int:
        pass
