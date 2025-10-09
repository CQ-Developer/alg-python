from abc import ABC, abstractmethod

class Solution(ABC):

    @abstractmethod
    def numberOfSubarrays(self, nums:list[int])-> int:
        pass