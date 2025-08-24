from src.leetcode.n1472.solution import BrowserHistory
from unittest import TestCase


class TestBrowserHistory(TestCase):
    browser: BrowserHistory

    def setUp(self):
        self.browser = BrowserHistory('leetcode.com')

    def test_1(self):
        self.browser.visit("google.com")
        self.browser.visit("facebook.com")
        self.browser.visit("youtube.com")
        self.assertEqual('facebook.com', self.browser.back(1))
        self.assertEqual('google.com', self.browser.back(1))
        self.assertEqual('facebook.com', self.browser.forward(1))
        self.browser.visit("linkedin.com")
        self.assertEqual('linkedin.com', self.browser.forward(2))
        self.assertEqual('google.com', self.browser.back(2))
        self.assertEqual('leetcode.com', self.browser.back(7))
