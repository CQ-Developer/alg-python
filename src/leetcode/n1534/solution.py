from abc import ABC, abstractmethod
from typing import override


class Solution(ABC):

    @abstractmethod
    def count_good_triplets(self, arr: list[int], a: int, b: int, c: int) -> int:
        pass


class SolutionA(Solution):
    """
    暴力
    """

    @override
    def count_good_triplets(self, arr: list[int], a: int, b: int, c: int) -> int:
        cnt = 0
        for i, x in enumerate(arr):
            for j, y in enumerate(arr[i + 1 :], i + 1):
                for z in arr[j + 1 :]:
                    if abs(x - y) <= a and abs(y - z) <= b and abs(x - z) <= c:
                        cnt += 1
        return cnt


class SolutionB(Solution):
    """
    前缀和
    """

    @override
    def count_good_triplets(self, arr: list[int], a: int, b: int, c: int) -> int:
        mx = max(arr)
        s = [0] * (mx + 2)
        ans = 0
        for j, y in enumerate(arr):
            for z in arr[j + 1 :]:
                if abs(y - z) > b:
                    continue
                l, r = max(y - a, z - c, 0), min(y + a, z + c, mx)
                ans += max(s[r + 1] - s[l], 0)
            for v in range(y + 1, mx + 2):
                s[v] += 1
        return ans


class SolutionC(Solution):
    """
    排序 + 3指针 + 枚举j
    """

    @override
    def count_good_triplets(self, arr: list[int], a: int, b: int, c: int) -> int:
        idx = sorted(range(len(arr)), key=lambda i: arr[i])
        ans = 0
        for j in idx:
            left = [arr[i] for i in idx if i < j and abs(arr[i] - arr[j]) <= a]
            right = [arr[k] for k in idx if k > j and abs(arr[j] - arr[k]) <= b]
            p1 = p2 = 0
            for x in left:
                while p2 < len(right) and right[p2] <= x + c:
                    p2 += 1
                while p1 < len(right) and right[p1] < x - c:
                    p1 += 1
                ans += p2 - p1
        return ans
