import abc
import typing


class Solution(abc.ABC):
    @abc.abstractmethod
    def can_make_pali_queries(self, s: str, queries: list[list[int]]) -> list[bool]:
        pass


class SolutionA(Solution):
    """
    偶数情况
        假设字符串中有偶数个a, 由于可以重排列子串,
        那么这偶数个 a 一定可以构成回文串

    奇数情况
        1. 假设只有 a 出现奇数次, 其余字母都出现偶数次,
           那么可以将多出的 a 放在字符串的中心,
           形成回文串
        2. 将设存在两种字母 a 和 b 出现奇数次,
           可以通过将 a 改成 b 的方式构成回文串
        3. 假设存在三种字母 a/b/c 出现奇数次,
           可以先通过方法二在通过方法一,
           将结果变为回文串
        得到结论: 如果有 m 中字母出现奇数次,
                  只需要将 m // 2 个字母进行替换
                  就能构成回文串, 根据题目要求得到 (m // 2) <= k
    """

    @typing.override
    def can_make_pali_queries(self, s: str, queries: list[list[int]]) -> list[bool]:
        pre = [[0] * 26]
        for c in s:
            pre.append([*pre[-1]])
            pre[-1][ord(c) - ord("a")] += 1
        ans = []
        for l, r, k in queries:
            m = 0
            for sl, sr in zip(pre[l], pre[r + 1]):
                m += (sr - sl) % 2
            ans.append(m // 2 <= k)
        return ans


class SolutionB(Solution):
    """
    由于只关心奇偶性, 使用位运算优化
    """

    @typing.override
    def can_make_pali_queries(self, s: str, queries: list[list[int]]) -> list[bool]:
        pre = [[0] * 26]
        for c in s:
            pre.append([*pre[-1]])
            pre[-1][ord(c) - ord("a")] ^= 1
        ans = []
        for l, r, k in queries:
            m = 0
            for sl, sr in zip(pre[l], pre[r + 1]):
                m += sr ^ sl
            ans.append(m // 2 <= k)
        return ans


class SolutionC(Solution):
    """
    更纯粹的位运算优化
    """

    @typing.override
    def can_make_pali_queries(self, s: str, queries: list[list[int]]) -> list[bool]:
        n = len(s)
        pre = [0] * (n + 1)
        for i, c in enumerate(s):
            b = 1 << (ord(c) - ord("a"))
            pre[i + 1] = pre[i] ^ b
        ans = []
        for l, r, k in queries:
            mask = pre[r + 1] ^ pre[l]
            odd = mask.bit_count()
            ans.append(odd // 2 <= k)
        return ans
