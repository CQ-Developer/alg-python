from abc import ABC, abstractmethod


class Solution(ABC):

    @abstractmethod
    def find_peak_element(self, nums: list[int]) -> int:
        pass
