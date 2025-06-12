from abc import ABC, abstractmethod


class Solution(ABC):

    @abstractmethod
    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
        pass
