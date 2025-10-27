from abc import ABC, abstractmethod
from typing import override


class Solution(ABC):

    @abstractmethod
    def maximum_length_of_ranges(self, nums: list[int]) -> list[int]:
        pass


class SolutionA(Solution):

    @override
    def maximum_length_of_ranges(self, nums: list[int]) -> list[int]:
        n = len(nums)
        ans = [-1] * n
        st = []
        for i, x in enumerate(nums):
            while st and x > nums[st[-1]]:
                st.pop()
            if st:
                ans[i] = st[-1]
            st.append(i)
        st.clear()
        for i in range(n - 1, -1, -1):
            while st and nums[i] > nums[st[-1]]:
                st.pop()
            ans[i] = (st[-1] - ans[i] if st else n - ans[i]) - 1
            st.append(i)
        return ans
