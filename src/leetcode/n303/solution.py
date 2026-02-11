from itertools import accumulate


class NumArray:

    def __init__(self, nums: list[int]):
        self.pre = list(accumulate(nums, initial=0))

    def sum_range(self, left: int, right: int) -> int:
        return self.pre[right + 1] - self.pre[left]
