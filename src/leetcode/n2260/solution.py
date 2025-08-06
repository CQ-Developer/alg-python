from abc import ABC, abstractmethod


class Solution(ABC):

    @abstractmethod
    def minimum_card_pickup(self, cards: list[int]) -> int:
        pass
