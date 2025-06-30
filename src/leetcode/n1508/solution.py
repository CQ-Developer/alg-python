import heapq
from abc import ABC, abstractmethod
from typing import override


class Solution(ABC):

    @abstractmethod
    def range_sum(self, nums: list[int], n: int, left: int, right: int) -> int:
        pass


class SolutionA(Solution):

    @override
    def range_sum(self, nums: list[int], n: int, left: int, right: int) -> int:
        h: list[tuple[int, int]] = []
        for i, x in enumerate(nums):
            heapq.heappush(h, (x, i))
        s = 0
        for j in range(1, right + 1):
            x, i = heapq.heappop(h)
            if j >= left:
                s += x
            if i + 1 < n:
                heapq.heappush(h, (x + nums[i + 1], i + 1))
        return s % 1000000007


class SolutionB(Solution):

    @override
    def range_sum(self, nums: list[int], n: int, left: int, right: int) -> int:
        p, pp = [0], [0]
        for x in nums:
            p.append(p[-1] + x)
            pp.append(pp[-1] + p[-1])

        def get_sum_cnt(x: int) -> tuple[int, int]:
            j = s = cnt = 0
            for i, v in enumerate(p):
                while j < n and p[j + 1] - v < x:
                    j += 1
                s += pp[j] - pp[i] - (j - i) * v
                cnt += j - i
            return s, cnt

        def get_kth(k: int) -> int:
            '''
            (l...r]
            '''
            l, r = 0, p[n]
            while l < r:
                mid = (l + r + 1) // 2
                _, cnt = get_sum_cnt(mid)
                if cnt >= k:
                    r = mid - 1
                else:
                    l = mid
            return l

        def f(k: int) -> int:
            x = get_kth(k)
            s, cnt = get_sum_cnt(x)
            return s + (k - cnt) * x

        return (f(right) - f(left - 1)) % 1000000007
