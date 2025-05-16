class Solution:
    def minimizeArrayValue(self, nums: list[int]) -> int:
        def check(mid: int) -> bool:
            rest = 0
            for i in range(len(nums) - 1, 0, -1):
                rest = max(0, nums[i] + rest - mid)
            return nums[0] + rest <= mid

        l, r = min(nums), max(nums)
        while l < r:
            m = (l + r) // 2
            if check(m):
                r = m
            else:
                l = m + 1
        return r
