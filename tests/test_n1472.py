import copy
import json
from pathlib import Path
from typing import TypedDict

import pytest

from src.n1472 import BrowserHistory


class TestCase(TypedDict):
    __test__ = False
    init: list[str]
    operations: list[str]
    arguments: list[list[int] | list[str]]
    expected: list[str | None]


def _load_test_cases() -> list[TestCase]:
    case_name = Path(__file__).stem.removeprefix("test_")
    case_file = Path(__file__).parent / "cases" / f"{case_name}.json"
    return json.loads(case_file.read_text(encoding="utf-8"))


@pytest.mark.parametrize("case", _load_test_cases())
def test_browser_history(case: TestCase):
    case = copy.deepcopy(case)
    browser_history = BrowserHistory(*case["init"])
    actual = [
        getattr(browser_history, operation)(*arguments)
        for operation, arguments in zip(case["operations"], case["arguments"])
    ]
    assert actual == case["expected"]
