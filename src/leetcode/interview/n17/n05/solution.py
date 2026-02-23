from abc import ABC, abstractmethod
from typing import override


class Solution(ABC):

    @abstractmethod
    def find_longest_subarray(self, array: list[str]) -> list[str]:
        pass


class SolutionA(Solution):

    @override
    def find_longest_subarray(self, array: list[str]) -> list[str]:
        p = n = pre = 0
        cnt = {0: -1}
        for i, x in enumerate(array):
            pre += 1 if x.isdigit() else -1
            if pre in cnt:
                j = cnt[pre]
                m = i - j
                if m > n:
                    p, n = j, m
            else:
                cnt[pre] = i
        return array[p + 1 : p + 1 + n]
