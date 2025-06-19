import heapq
from abc import ABC, abstractmethod
from typing import override
from itertools import islice


class Solution(ABC):

    @abstractmethod
    def kth_smallest(self, mat: list[list[int]], k: int) -> int:
        pass


class SolutionA(Solution):

    @override
    def kth_smallest(self, mat: list[list[int]], k: int) -> int:
        res = mat[0][:k]
        for row in islice(mat, 1, None):
            res = sorted(x + y for x in res for y in row)[:k]
        return res[-1]


class SolutionB(Solution):

    @override
    def kth_smallest(self, mat: list[list[int]], k: int) -> int:
        m = len(mat)

        def check(i: int, r: int) -> int:
            if i == m:
                return 1
            ans = 0
            for x in mat[i]:
                if x - mat[i][0] > r or ans >= k:
                    break
                ans += check(i + 1, r - x + mat[i][0])
            return ans

        l, r = map(sum, zip(*((row[0], row[-1]) for row in mat)))
        s = l
        while l <= r:
            mid = (l + r) // 2
            if check(0, mid - s) >= k:
                r = mid - 1
            else:
                l = mid + 1
        return l


class SolutionC(Solution):

    @override
    def kth_smallest(self, mat: list[list[int]], k: int) -> int:
        def kth_smallest_pairs(a: list[int], b: list[int]) -> list[int]:
            ans: list[int] = []
            h = [(a[0] + b[0], 0, 0)]
            while h and len(ans) < k:
                _, i, j = heapq.heappop(h)
                ans.append(a[i] + b[j])
                if j == 0 and i + 1 < len(a):
                    heapq.heappush(h, (a[i + 1] + b[0], i + 1, 0))
                if j + 1 < len(b):
                    heapq.heappush(h, (a[i] + b[j + 1], i, j + 1))
            return ans

        ans = mat[0][:k]
        for row in islice(mat, 1, None):
            ans = kth_smallest_pairs(ans, row)
        return ans[-1]
