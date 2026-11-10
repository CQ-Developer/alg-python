import copy
import json
from pathlib import Path
from typing import Any, TypedDict

import pytest

from src.n901 import StockSpanner, StockSpannerA


class TestCase(TypedDict):
    __test__ = False
    init: list[Any]
    operations: list[str]
    arguments: list[list[int]]
    expected: list[int]


def _load_test_cases() -> list[TestCase]:
    case_name = Path(__file__).stem.removeprefix("test_")
    case_file = Path(__file__).parent / "cases" / f"{case_name}.json"
    return json.loads(case_file.read_text(encoding="utf-8"))


@pytest.fixture(params=[StockSpannerA])
def stock_spanner_cls(request: pytest.FixtureRequest) -> type[StockSpanner]:
    return request.param


@pytest.mark.parametrize("case", _load_test_cases())
def test_stock_spanner(stock_spanner_cls: type[StockSpanner], case: TestCase):
    case = copy.deepcopy(case)
    stock_spanner = stock_spanner_cls(*case["init"])
    actual = [
        getattr(stock_spanner, operation)(*arguments)
        for operation, arguments in zip(case["operations"], case["arguments"])
    ]
    assert actual == case["expected"]
