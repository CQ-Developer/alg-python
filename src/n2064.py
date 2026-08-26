class Solution:
    def minimizedMaximum(self, n: int, quantities: list[int]) -> int:
        def check(x: int) -> bool:
            cnt = len(quantities)
            for q in quantities:
                cnt += (q - 1) // x
                if cnt > n:
                    return False
            return True

        l, r = 1, max(quantities)
        while l <= r:
            m = (l + r) // 2
            if check(m):
                r = m - 1
            else:
                l = m + 1
        return l
