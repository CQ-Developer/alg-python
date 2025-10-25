from abc import ABC, abstractmethod
from typing import override


class Solution(ABC):

    @abstractmethod
    def max_score(self, nums: list[int]) -> int:
        pass


class SolutionA(Solution):

    @override
    def max_score(self, nums: list[int]) -> int:
        n = len(nums)
        st = []
        for i, x in enumerate(nums):
            while st and x >= nums[st[-1]]:
                st.pop()
            st.append(i)
        ans, i = 0, 0
        for j in st:
            ans += (j - i) * nums[j]
            i = j
        return ans
