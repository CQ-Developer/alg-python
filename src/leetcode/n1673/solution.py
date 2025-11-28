from abc import ABC, abstractmethod
from typing import override


class Solution(ABC):

    @abstractmethod
    def most_competitive(self, nums: list[int], k: int) -> list[int]:
        pass


class SolutonA(Solution):

    @override
    def most_competitive(self, nums: list[int], k: int) -> list[int]:
        st = []
        for i, x in enumerate(nums):
            while st and x < st[-1] and len(st) + len(nums) - i > k:
                st.pop()
            if len(st) < k:
                st.append(x)
        return st
