from src.solution_n1472 import BrowserHistory


def test_1():
    browser = BrowserHistory('leetcode.com')
    browser.visit('google.com')
    browser.visit('facebook.com')
    browser.visit('youtube.com')
    assert 'facebook.com' == browser.back(1)
    assert 'google.com' == browser.back(1)
    assert 'facebook.com' == browser.forward(1)
    browser.visit('linkedin.com')
    assert 'linkedin.com' == browser.forward(2)
    assert 'google.com' == browser.back(2)
    assert 'leetcode.com' == browser.back(7)
