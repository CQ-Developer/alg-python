from abc import ABC, abstractmethod
from collections import Counter
from itertools import accumulate
from operator import xor
from typing import override


class Solution(ABC):
    @abstractmethod
    def count_triplets(self, arr: list[int]) -> int:
        pass


class SolutionA(Solution):
    @override
    def count_triplets(self, arr: list[int]) -> int:
        p = list(accumulate(arr, xor, initial=0))
        ans, n = 0, len(arr)
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j, n):
                    if p[j] ^ p[i] == p[k + 1] ^ p[j]:
                        ans += 1
        return ans


class SolutionB(Solution):
    @override
    def count_triplets(self, arr: list[int]) -> int:
        p = list(accumulate(arr, xor, initial=0))
        a, n = 0, len(arr)
        for i in range(n):
            for k in range(i + 1, n):
                if p[k + 1] == p[i]:
                    a += k - i
        return a


class SolutionC(Solution):
    @override
    def count_triplets(self, arr: list[int]) -> int:
        cnt, all = Counter(), Counter()
        pre = ans = 0
        for i, x in enumerate(arr):
            cnt[pre] += 1
            all[pre] += i
            pre ^= x
            ans += i * cnt[pre] - all[pre]
        return ans
