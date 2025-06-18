import heapq
from abc import ABC, abstractmethod
from typing import override
from itertools import islice


class Solution(ABC):

    @abstractmethod
    def kSmallestPairs(self, nums1: list[int], nums2: list[int], k: int) -> list[list[int]]:
        pass


class SolutionA(Solution):

    @override
    def kSmallestPairs(self, nums1: list[int], nums2: list[int], k: int) -> list[list[int]]:
        h = [(x + nums2[0], i, 0) for i, x in enumerate(islice(nums1, k))]
        res: list[list[int]] = []
        while len(res) < k:
            _, i, j = heapq.heappop(h)
            res.append([nums1[i], nums2[j]])
            if j + 1 < len(nums2):
                heapq.heappush(h, (nums1[i] + nums2[j + 1], i, j + 1))
        return res


class SolutionB(Solution):

    @override
    def kSmallestPairs(self, nums1: list[int], nums2: list[int], k: int) -> list[list[int]]:
        m, n = len(nums1), len(nums2)
        hp = [(nums1[0] + nums2[0], 0, 0)]
        res: list[list[int]] = []
        while len(res) < k:
            _, i, j = heapq.heappop(hp)
            res.append([nums1[i], nums2[j]])
            if j == 0 and i + 1 < m:
                heapq.heappush(hp, (nums1[i + 1] + nums2[0], i + 1, 0))
            if j + 1 < n:
                heapq.heappush(hp, (nums1[i] + nums2[j + 1], i, j + 1))
        return res


class SolutionC(Solution):

    @override
    def kSmallestPairs(self, nums1: list[int], nums2: list[int], k: int) -> list[list[int]]:
        m, n = len(nums1), len(nums2)

        def check(x: int) -> int:
            cnt, l, r = 0, 0, n - 1
            while l < m and r >= 0:
                if nums1[l] + nums2[r] > x:
                    r -= 1
                else:
                    l += 1
                    cnt += r + 1
            return cnt

        left, right = nums1[0] + nums2[0], nums1[-1] + nums2[-1]
        while left <= right:
            mid = (left + right) // 2
            if check(mid) >= k:
                right = mid - 1
            else:
                left = mid + 1
        res: list[list[int]] = []
        r = n - 1
        for x in nums1:
            while r >= 0 and x + nums2[r] >= left:
                r -= 1
            for y in islice(nums2, r + 1):
                res.append([x, y])
                if len(res) == k:
                    return res
        r = n - 1
        for x in nums1:
            while r >= 0 and x + nums2[r] > left:
                r -= 1
            i = r
            while i >= 0 and x + nums2[i] == left:
                res.append([x, nums2[i]])
                if len(res) == k:
                    return res
                i -= 1
        return res
