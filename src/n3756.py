import abc
import typing


class Solution(abc.ABC):
    """
    给你一个长度为 `m` 的字符串 `s`, 其中仅包含数字.
    另给你一个二维整数数组 `queries`, 其中 $queries[i] = [l_i, r_i]$.

    对于每个 `queries[i]`, 提取子串 $s[l_i ... r_i]$, 然后执行以下操作:
    - 将字串中所有非零数字按照原始顺序连接起来, 形成一个新的整数 `x`. 如果没有非零数字, 则 `x = 0`.
    - 令 `sum` 为 `x` 中所有数字的数字和. 答案为 `x * sum`.

    返回一个整数数组 `answer`, 其中 `answer[i]` 是第 `i` 个查询的答案.

    由于答案可能非常大, 请返回其对 $10^9 + 7$ 取余数的结果.

    子串是字符串中的一个连续, 非空字符序列.
    """

    @abc.abstractmethod
    def sum_and_multiply(self, s: str, queries: list[list[int]]) -> list[int]:
        pass


mod = 1_000_000_007
pow10 = [1]
for i in range(1, 100_001):
    pow10.append(pow10[-1] * 10 % mod)


class SolutionA(Solution):
    """
    暴力
    """

    @typing.override
    def sum_and_multiply(self, s: str, queries: list[list[int]]) -> list[int]:
        ans = []
        for l, r in queries:
            p, f, m = 0, 0, 10
            for x in (ord(c) - 48 for c in s[l : r + 1]):
                p += x
                if x:
                    f = f * m + x
            ans.append(f * p % mod)
        return ans


class SolutionB(Solution):
    """
    前缀和
    """

    @typing.override
    def sum_and_multiply(self, s: str, queries: list[list[int]]) -> list[int]:
        pre_sum = [0]
        pre_num = [0]
        non_len = [0]
        for x in (ord(c) - 48 for c in s):
            pre_sum.append(pre_sum[-1] + x)
            pre_num.append(((pre_num[-1] * 10 + x) % mod) if x else pre_num[-1])
            non_len.append(non_len[-1] + (x > 0))
        ans = []
        for l, r in queries:
            n = non_len[r + 1] - non_len[l]
            a = pre_num[r + 1] - pre_num[l] * pow10[n]
            ans.append(a * (pre_sum[r + 1] - pre_sum[l]) % mod)
        return ans
