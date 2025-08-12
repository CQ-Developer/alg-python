from abc import ABC, abstractmethod
from collections import defaultdict, Counter
from typing import override


class Solution(ABC):

    @abstractmethod
    def similar_pairs(self, words: list[str]) -> int:
        pass


class SolutionA(Solution):

    @override
    def similar_pairs(self, words: list[str]) -> int:
        res = 0
        cnt = defaultdict(int)
        for w in words:
            k = 0
            for c in w:
                k |= 1 << (ord(c) & 0x1f)
            res += cnt[k]
            cnt[k] += 1
        return res


class SolutionB(Solution):

    @override
    def similar_pairs(self, words: list[str]) -> int:
        cnt = Counter(frozenset(w) for w in words)
        return sum(c * (c - 1) // 2 for c in cnt.values() if c > 1)
