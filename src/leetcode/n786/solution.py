import heapq
from abc import ABC, abstractmethod
from typing import override
from itertools import islice


class Solution(ABC):

    @abstractmethod
    def kth_smallest_prime_fraction(self, arr: list[int], k: int) -> list[int]:
        pass


class Frac:

    def __init__(self, i: int, j: int, x: int, y: int) -> None:
        self.i = i
        self.j = j
        self.x = x
        self.y = y

    def __lt__(self, other: 'Frac') -> bool:
        return self.x * other.y < other.x * self.y


class SolutionA(Solution):

    @override
    def kth_smallest_prime_fraction(self, arr: list[int], k: int) -> list[int]:
        h = [Frac(0, j + 1, arr[0], y) for j, y in enumerate(arr[1:])]
        heapq.heapify(h)
        for _ in range(1, k):
            frac = heapq.heappop(h)
            i, j = frac.i, frac.j
            if i + 1 < j:
                heapq.heappush(h, Frac(i + 1, j, arr[i + 1], arr[j]))
        return [h[0].x, h[0].y]


class SolutionB(Solution):

    @override
    def kth_smallest_prime_fraction(self, arr: list[int], k: int) -> list[int]:
        l, r = 0, 1
        while True:
            mid = (l + r) / 2
            i, x, y, cnt = 0, 0, 1, 0
            for v in islice(arr, 1, None):
                while arr[i] / v < mid:
                    if arr[i] * y > x * v:
                        x, y = arr[i], v
                    i += 1
                cnt += i
            if cnt == k:
                return [x, y]
            if cnt < k:
                l = mid
            else:
                r = mid
