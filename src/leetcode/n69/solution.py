from abc import ABC, abstractmethod


class Solution(ABC):

    @abstractmethod
    def my_sqrt(self, x: int) -> int:
        pass
