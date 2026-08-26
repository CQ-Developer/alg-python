import abc
import typing


class Solution(abc.ABC):
    """
    Given the string s, return the size of the longest substring
    containing each vowel and even number of times.
    That is, 'a', 'e', 'i', 'o', and 'u' must appear an even
    number of times.

    1 <= s.length <= 5 * 10^5
    s contains only lowercase English letters
    """

    @abc.abstractmethod
    def find_the_longest_substring(self, s: str) -> int:
        pass


class SolutionA(Solution):
    @typing.override
    def find_the_longest_substring(self, s: str) -> int:
        vowel = {"a": 1, "e": 2, "i": 4, "o": 8, "u": 16}
        pos = [-1] * (1 << 5)
        ans = st = pos[0] = 0
        for i, c in enumerate(s):
            st ^= vowel.get(c, 0)
            if pos[st] >= 0:
                ans = max(ans, i + 1 - pos[st])
            else:
                pos[st] = i + 1
        return ans
