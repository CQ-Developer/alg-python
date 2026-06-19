from abc import ABC, abstractmethod
from typing import override
from itertools import accumulate
from collections import defaultdict


class Solution(ABC):
	"""
	请和为k的子数组数量
	"""

	@abstractmethod
	def subarray_sum(self, nums: list[int], k: int) -> int:
		pass


class SolutionA(Solution):
	"""
	两次遍历
	"""

	@override
	def subarray_sum(self, nums: list[int], k: int) -> int:
		ans = 0
		cnt = defaultdict(int)
		for x in accumulate(nums, initial=0):
			ans += cnt[x - k]
			cnt[x] += 1
		return ans


class SolutionB(Solution):
	"""
	一次遍历
	"""

	@override
	def subarray_sum(self, nums: list[int], k: int) -> int:
		a = p = 0
		cnt = defaultdict(int)
		for x in nums:
			cnt[p] += 1
			p += x
			a += cnt[p - k]
		return a
