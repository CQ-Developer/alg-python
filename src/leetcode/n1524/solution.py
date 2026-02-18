from abc import ABC, abstractmethod
from typing import override


class Solution(ABC):

    @abstractmethod
    def num_of_subarrays(self, arr: list[int]) -> int:
        pass


class SolutionA(Solution):

    @override
    def num_of_subarrays(self, arr: list[int]) -> int:
        cnt = pre = even = odd = 0
        for x in arr:
            pre += x
            if pre % 2 == 1:
                # 奇数
                odd += 1
                cnt += even + 1
            else:
                # 偶数
                even += 1
                cnt += odd
        return cnt % (10**9 + 7)
