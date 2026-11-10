import pytest

from src.n1472 import BrowserHistory
from tests.case_loader import Case, load_cases


@pytest.mark.parametrize("case", load_cases(__file__))
def test_browser_history(case: Case):
    browser_history = BrowserHistory(*case["init"])
    actual = [
        getattr(browser_history, operation)(*arguments)
        for operation, arguments in zip(case["operations"], case["arguments"])
    ]
    assert actual == case["expected"]
