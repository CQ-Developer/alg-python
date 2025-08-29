from abc import ABC, abstractmethod
from typing import override
from collections import defaultdict


class Solution(ABC):

    @abstractmethod
    def max_chunks_to_sorted(self, arr: list[int]) -> int:
        pass


class SolutionA(Solution):

    @override
    def max_chunks_to_sorted(self, arr: list[int]) -> int:
        cnt = defaultdict(int)
        res = 0
        for x, y in zip(arr, sorted(arr)):
            cnt[x] += 1
            if not cnt[x]:
                del cnt[x]
            cnt[y] -= 1
            if not cnt[y]:
                del cnt[y]
            if not cnt:
                res += 1
        return res


class SolutionB(Solution):

    @override
    def max_chunks_to_sorted(self, arr: list[int]) -> int:
        stk = []
        for x in arr:
            if not stk or x >= stk[-1]:
                stk.append(x)
            else:
                y = stk[-1]
                while stk and stk[-1] > x:
                    stk.pop()
                stk.append(y)
        return len(stk)
