from abc import ABC, abstractmethod


class Solution(ABC):

    @abstractmethod
    def preimageSizeFZF(self, k: int) -> int:
        pass
