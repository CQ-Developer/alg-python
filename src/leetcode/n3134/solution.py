from abc import ABC, abstractmethod
from typing import override
from collections import Counter
from bisect import bisect_left


class Solution(ABC):

    @abstractmethod
    def median_of_uniqueness_array(self, nums: list[int]) -> int:
        pass


class SolutionA(Solution):

    @override
    def median_of_uniqueness_array(self, nums: list[int]) -> int:
        n = len(nums)
        k = (n * (n + 1) // 2 + 1) // 2

        def check(up: int) -> bool:
            freq: Counter[int] = Counter()
            l = cnt = 0
            for r, _in in enumerate(nums):
                freq[_in] += 1
                while len(freq) > up:
                    _out = nums[l]
                    freq[_out] -= 1
                    if freq[_out] == 0:
                        del freq[_out]
                    l += 1
                cnt += r - l + 1
                if cnt >= k:
                    return True
            return False

        return bisect_left(range(len(set(nums))), True, 1, key=check)
