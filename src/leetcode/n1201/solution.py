from abc import ABC, abstractmethod


class Solution(ABC):

    @abstractmethod
    def nthUglyNumber(self, n: int, a: int, b: int, c: int):
        pass
