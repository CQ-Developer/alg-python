class Solution:
    def minimumSize(self, nums: list[int], maxOperations: int) -> int:
        l, r = 1, max(nums)
        while l <= r:
            m = (l + r) // 2
            if sum((num - 1) // m for num in nums) <= maxOperations:
                r = m - 1
            else:
                l = m + 1
        return l
