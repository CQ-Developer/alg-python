from abc import ABC, abstractmethod


class Solution(ABC):

    @abstractmethod
    def kth_smallest_prime_fraction(self, arr: list[int], k: int) -> list[int]:
        pass
