import abc
import typing


class Solution(abc.ABC):
    @abc.abstractmethod
    def wonderful_substrings(self, word: str) -> int:
        pass


class SolutionA(Solution):
    @typing.override
    def wonderful_substrings(self, word: str) -> int:
        cnt = [0] * (1 << 10)
        cnt[0] = 1
        st = ans = 0
        for i, c in enumerate(ord(x) - 97 for x in word):
            st ^= 1 << c
            ans += cnt[st]
            for j in range(10):
                ans += cnt[st ^ (1 << j)]
            cnt[st] += 1
        return ans
