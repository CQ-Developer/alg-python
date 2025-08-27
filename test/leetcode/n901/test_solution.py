from src.leetcode.n901.solution import StockSpanner, StockSpannerA
from unittest import TestCase, SkipTest


class TestStockSpanner(TestCase):
    spanner: StockSpanner

    @classmethod
    def setUpClass(cls):
        if cls is TestStockSpanner:
            raise SkipTest('skip')

    def test_1(self):
        self.assertEqual(1, self.spanner.next(100))
        self.assertEqual(1, self.spanner.next(80))
        self.assertEqual(1, self.spanner.next(60))
        self.assertEqual(2, self.spanner.next(70))
        self.assertEqual(1, self.spanner.next(60))
        self.assertEqual(4, self.spanner.next(75))
        self.assertEqual(6, self.spanner.next(85))


class TestStockSpannerA(TestStockSpanner):

    def setUp(self):
        self.spanner = StockSpannerA()
