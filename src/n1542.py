import abc
import typing


class Solution(abc.ABC):
    @abc.abstractmethod
    def longest_awesome(self, s: str) -> int:
        pass


class SolutionA(Solution):
    """
    回文串长度为偶数
        pos[j] ^ pos[i] == 0
    回文串长度为奇数
        ( pos[j] ^ pos[i] ).bit_count() == 1
    """

    @typing.override
    def longest_awesome(self, s: str) -> int:
        pos = {0: -1}
        st = ans = 0
        for i, x in enumerate(int(c) for c in s):
            st ^= 1 << x
            # 奇数
            for j in range(10):
                _st = st ^ (1 << j)
                if _st in pos:
                    ans = max(ans, i - pos[_st])
            # 偶数
            if st in pos:
                ans = max(ans, i - pos[st])
            else:
                pos[st] = i
        return ans
