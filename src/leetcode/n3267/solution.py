from abc import ABC, abstractmethod
from typing import override
from collections import defaultdict


class Solution(ABC):

    @abstractmethod
    def count_pair(self, nums: list[int]) -> int:
        pass


class SolutionA(Solution):

    @override
    def count_pair(self, nums: list[int]) -> int:
        nums.sort()
        res = 0
        cnt = defaultdict(int)
        for x in nums:
            p = {x}
            s = list(str(x))
            n = len(s)
            for i in range(n):
                for j in range(i + 1, n):
                    if s[i] == s[j]:
                        continue
                    s[i], s[j] = s[j], s[i]
                    p.add(int(''.join(s)))
                    for k in range(i + 1, n):
                        for l in range(k + 1, n):
                            if s[k] == s[l]:
                                continue
                            s[k], s[l] = s[l], s[k]
                            p.add(int(''.join(s)))
                            s[k], s[l] = s[l], s[k]
                    s[i], s[j] = s[j], s[i]
            res += sum(cnt[k] for k in p)
            cnt[x] += 1
        return res


class SolutionB(Solution):
    p = (1, 10, 100, 1000, 10000, 100000, 1000000)

    @override
    def count_pair(self, nums: list[int]) -> int:
        nums.sort()
        res = 0
        cnt = defaultdict(int)
        for x in nums:
            st = {x}
            a = list(map(int, str(x)))[::-1]
            n = len(a)
            for i in range(n):
                for j in range(i + 1, n):
                    if a[i] == a[j]:
                        continue
                    y = x + (a[j] - a[i]) * (SolutionB.p[i] - SolutionB.p[j])
                    st.add(y)
                    a[i], a[j] = a[j], a[i]
                    for k in range(i + 1, n):
                        for l in range(k + 1, n):
                            st.add(y + (a[l] - a[k]) * (SolutionB.p[k] - SolutionB.p[l]))
                    a[i], a[j] = a[j], a[i]
            res += sum(cnt[v] for v in st)
            cnt[x] += 1
        return res


class SolutionC(Solution):
    p = (1, 10, 100, 1000, 10000, 100000, 1000000)

    @override
    def count_pair(self, nums: list[int]) -> int:
        res = 0
        n = len(str(max(nums)))
        bit_num = defaultdict(int)
        for p, x in enumerate(nums):
            s = {x}
            a = list(map(int, str(x).zfill(n)))
            a.reverse()
            for i in range(n - 1):
                for j in range(i + 1, n):
                    if a[i] == a[j]:
                        continue
                    s.add(x + (a[j] - a[i]) * (SolutionC.p[i] - SolutionC.p[j]))
            idx, bp = 0, 1 << p
            for v in s:
                idx |= bit_num[v]
                bit_num[v] |= bp
            res += idx.bit_count()
        return res
