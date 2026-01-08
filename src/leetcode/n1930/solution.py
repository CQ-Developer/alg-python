from abc import ABC, abstractmethod
from typing import override
from string import ascii_lowercase
from collections import Counter, defaultdict


class Solution(ABC):

    @abstractmethod
    def count_palindromic_subsequence(self, s: str) -> int:
        pass


class SolutionA(Solution):

    @override
    def count_palindromic_subsequence(self, s: str) -> int:
        cnt = 0
        for c in ascii_lowercase:
            l = s.find(c)
            if l >= 0:
                r = s.rfind(c)
                cnt += len(set(s[l + 1 : r]))
        return cnt


class SolutionB(Solution):

    @override
    def count_palindromic_subsequence(self, s: str) -> int:
        st = set()
        right, left = Counter(s), set()
        for i in s:
            right[i] -= 1
            if right[i] == 0:
                del right[i]
            for j in left & right.keys():
                st.add(j + i)
            left.add(i)
        return len(st)


class SolutionC(Solution):

    @override
    def count_palindromic_subsequence(self, s: str) -> int:
        r, right = 0, defaultdict(int)
        for c in map(ord, s):
            right[c] += 1
            r |= 1 << c
        l, mask = 0, defaultdict(int)
        for c in map(ord, s):
            right[c] -= 1
            if right[c] == 0:
                r ^= 1 << c
            mask[c] |= l & r
            l |= 1 << c
        return sum(m.bit_count() for m in mask.values())
