from abc import ABC, abstractmethod
from typing import override
from itertools import pairwise
from bisect import bisect_left


class Solution(ABC):

    @abstractmethod
    def maxDistance(self, side: int, points: list[list[int]], k: int) -> int:
        pass


class SolutionA(Solution):

    @override
    def maxDistance(self, side: int, points: list[list[int]], k: int) -> int:
        n = len(points)
        arr: list[int] = []
        for x, y in points:
            if x == 0:
                arr.append(y)
            elif y == side:
                arr.append(side + x)
            elif x == side:
                arr.append(3 * side - y)
            else:
                arr.append(4 * side - x)
        arr.sort()

        def find(tar: int) -> int:
            l, r = -1, n
            while l + 1 < r:
                mid = (l + r) // 2
                if arr[mid] >= tar:
                    r = mid
                else:
                    l = mid
            return r

        def check(low: int) -> bool:
            idx = [0] * k
            for i, j in pairwise(range(k)):
                f = find(arr[idx[i]] + low)
                if f == n:
                    return False
                idx[j] = f
            if arr[idx[-1]] - arr[0] <= 4 * side - low:
                return True
            for i in range(1, idx[1]):
                idx[0] = i
                for p, j in pairwise(range(k)):
                    while arr[idx[j]] - arr[idx[p]] < low:
                        idx[j] += 1
                        if idx[j] == n:
                            return False
                if arr[idx[-1]] - arr[i] <= 4 * side - low:
                    return True
            return False

        l, r = 1, (4 * side) // k + 1
        while l + 1 < r:
            mid = (l + r) // 2
            if check(mid):
                l = mid
            else:
                r = mid
        return l


class SolutionB(Solution):

    @override
    def maxDistance(self, side: int, points: list[list[int]], k: int) -> int:
        n = len(points)
        arr: list[int] = []
        for x, y in points:
            if x == 0:
                arr.append(y)
            elif y == side:
                arr.append(side + x)
            elif x == side:
                arr.append(3 * side - y)
            else:
                arr.append(4 * side - x)
        arr.sort()

        def check(low: int) -> bool:
            print(low)
            idx = [0] * k
            for i, j in pairwise(range(k)):
                f = bisect_left(arr, arr[idx[i]] + low)
                if f == n:
                    return False
                idx[j] = f
            if arr[idx[-1]] - arr[0] <= 4 * side - low:
                return True
            for i in range(1, idx[1]):
                idx[0] = i
                for p, j in pairwise(range(k)):
                    while arr[idx[j]] - arr[idx[p]] < low:
                        idx[j] += 1
                        if idx[j] == n:
                            return False
                if arr[idx[-1]] - arr[i] <= 4 * side - low:
                    return True
            return False

        l, r = 1, (4 * side) // k + 1
        while l + 1 < r:
            mid = (l + r) // 2
            if check(mid):
                l = mid
            else:
                r = mid
        return l
