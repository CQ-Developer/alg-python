from abc import ABC, abstractmethod
from typing import override


class Solution(ABC):

    @abstractmethod
    def max_number(self, nums1: list[int], nums2: list[int], k: int) -> list[int]:
        pass


class SolutionA(Solution):

    @override
    def max_number(self, nums1: list[int], nums2: list[int], k: int) -> list[int]:
        return max(self._merge(self._peek_max(nums1, i), self._peek_max(nums2, k - i)) for i in range(k + 1) if i <= len(nums1) and k - i <= len(nums2))

    def _peek_max(self, num: list[int], k: int) -> list[int]:
        re = len(num) - k
        st = []
        for x in num:
            while re and st and x > st[-1]:
                st.pop()
                re -= 1
            st.append(x)
        return st[:k]

    def _merge(self, a: list[int], b: list[int]) -> list[int]:
        ans = []
        while a or b:
            c = a if a > b else b
            ans.append(c.pop(0))
        return ans
