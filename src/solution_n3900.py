from abc import ABC, abstractmethod
from collections import defaultdict
from typing import override


class Solution(ABC):
    @abstractmethod
    def longest_balanced(self, s: str) -> int:
        pass


class SolutionA(Solution):
    @override
    def longest_balanced(self, s: str) -> int:
        total_0 = s.count('0')
        total_1 = len(s) - total_0

        pos = defaultdict(list[int])
        pos[0] = [-1]

        ans = pre = 0

        for i, c in enumerate(s):
            pre += 1 if c == '1' else -1
            if len(pos[pre]) < 2:
                pos[pre].append(i)

            # 不交换
            ans = max(ans, i - pos[pre][0])

            # 字串1换0
            if pre - 2 in pos:
                p = pos[pre - 2]
                if (i - p[0] - 2) // 2 < total_0:
                    ans = max(ans, i - p[0])
                elif len(p) > 1:
                    ans = max(ans, i - p[1])

            # 字串0换1
            if pre + 2 in pos:
                p = pos[pre + 2]
                if (i - p[0] - 2) // 2 < total_1:
                    ans = max(ans, i - p[0])
                elif len(p) > 1:
                    ans = max(ans, i - p[1])

        return ans
