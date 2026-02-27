from abc import ABC, abstractmethod
from typing import override
from collections import defaultdict
from itertools import pairwise


class Solution(ABC):

    @abstractmethod
    def count_stable_subarrays(self, capacity: list[int]) -> int:
        pass


class SolutionA(Solution):

    @override
    def count_stable_subarrays(self, capacity: list[int]) -> int:
        ans = 0
        pre = capacity[0]
        cnt = defaultdict(int)
        for p, x in pairwise(capacity):
            ans += cnt[(x, pre)]
            cnt[(p, pre + p)] += 1
            pre += x
        return ans
