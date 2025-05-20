from abc import ABC, abstractmethod


class Solution(ABC):

    @abstractmethod
    def minimizeSet(self, divisor1: int, divisor2: int, uniqueCnt1: int, uniqueCnt2: int) -> int:
        pass
