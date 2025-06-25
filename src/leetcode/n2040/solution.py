from abc import ABC, abstractmethod
from typing import override
from bisect import bisect_left


class Solution(ABC):

    @abstractmethod
    def kth_smallest_product(self, nums1: list[int], nums2: list[int], k: int) -> int:
        pass


class SolutionA(Solution):

    @override
    def kth_smallest_product(self, nums1: list[int], nums2: list[int], k: int) -> int:
        x, y = bisect_left(nums1, 0), bisect_left(nums2, 0)
        m, n = len(nums1), len(nums2)

        def check(up: int) -> bool:
            cnt = 0
            if up < 0:
                i, j = 0, y
                while j < n and i < x:
                    if nums1[i] * nums2[j] > up:
                        j += 1
                    else:
                        i += 1
                        cnt += n - j
                i, j = x, 0
                while i < m and j < y:
                    if nums1[i] * nums2[j] > up:
                        i += 1
                    else:
                        j += 1
                        cnt += m - i
            else:
                cnt += x * (n - y) + y * (m - x)
                i, j = 0, y - 1
                while i < x and j >= 0:
                    if nums1[i] * nums2[j] > up:
                        i += 1
                    else:
                        j -= 1
                        cnt += x - i
                i, j = x, n - 1
                while i < m and j >= y:
                    if nums1[i] * nums2[j] > up:
                        j -= 1
                    else:
                        i += 1
                        cnt += j - y + 1
            return cnt >= k

        a, b, c, d = nums1[0] * nums2[0], nums1[-1] * nums2[-1], nums1[0] * nums2[-1], nums1[-1] * nums2[0]
        l, r = min(a, b, c, d), max(a, b, c, d)
        return l + bisect_left(range(l, r), True, key=check)
