import heapq
from abc import ABC, abstractmethod
from typing import override
from itertools import chain
from sortedcontainers import SortedList


class Solution(ABC):

    @abstractmethod
    def kthSmallest(self, matrix: list[list[int]], k: int) -> int:
        pass


class SolutionA(Solution):

    @override
    def kthSmallest(self, matrix: list[list[int]], k: int) -> int:
        arr = SortedList(chain.from_iterable(matrix))
        return arr[k - 1]


class SolutionB(Solution):

    @override
    def kthSmallest(self, matrix: list[list[int]], k: int) -> int:
        n = len(matrix)
        q = [(matrix[i][0], i, 0) for i in range(n)]
        heapq.heapify(q)
        for _ in range(k - 1):
            _, i, j = heapq.heappop(q)
            if j + 1 < n:
                heapq.heappush(q, (matrix[i][j + 1], i, j + 1))
        return heapq.heappop(q)[0]


class SolutionC(Solution):

    @override
    def kthSmallest(self, matrix: list[list[int]], k: int) -> int:
        n = len(matrix)

        def check(top: int) -> bool:
            i, j, cnt = n - 1, 0, 0
            while 0 <= i and j < n:
                if matrix[i][j] <= top:
                    cnt += i + 1
                    j += 1
                else:
                    i -= 1
            return cnt >= k

        l, r = matrix[0][0], matrix[-1][-1]
        while l <= r:
            mid = (l + r) // 2
            if check(mid):
                r = mid - 1
            else:
                l = mid + 1
        return l
