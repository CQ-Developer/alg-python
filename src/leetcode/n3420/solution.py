from abc import ABC, abstractmethod
from typing import override
from collections import deque


class Solution(ABC):

    @abstractmethod
    def count_non_decreasing_subarrays(self, nums: list[int], k: int) -> int:
        pass


class SolutionA(Solution):

    @override
    def count_non_decreasing_subarrays(self, nums: list[int], k: int) -> int:
        n = len(nums)

        g = [[] for _ in range(n)]
        pos_r = [n] * n
        st = []
        for i, x in enumerate(nums):
            while st and x >= nums[st[-1]]:
                pos_r[st.pop()] = i
            if st:
                g[st[-1]].append(i)
            st.append(i)

        cnt, ans, l = 0, 0, 0
        q = deque()
        for r, x in enumerate(nums):
            while q and x >= nums[q[-1]]:
                q.pop()
            q.append(r)

            cnt += nums[q[0]] - x

            while cnt > k:
                for i in g[l]:
                    if i > r:
                        break
                    cnt -= (nums[l] - nums[i]) * (min(pos_r[i], r + 1) - i)
                l += 1
                if q[0] < l:
                    q.popleft()
            ans += r - l + 1

        return ans


class SolutionB(Solution):

    @override
    def count_non_decreasing_subarrays(self, nums: list[int], k: int) -> int:
        n = len(nums)
        ans, cnt = 0, 0
        r = n - 1
        q = deque()
        for l in range(n - 1, -1, -1):
            x, m = nums[l], 1
            while q and x >= q[-1][0]:
                v, sz = q.pop()
                m += sz
                cnt += (x - v) * sz
            q.append([x, m])
            while cnt > k:
                tree = q[0]
                cnt -= tree[0] - nums[r]
                r -= 1
                tree[1] -= 1
                if tree[1] == 0:
                    q.popleft()
            ans += r - l + 1
        return ans
