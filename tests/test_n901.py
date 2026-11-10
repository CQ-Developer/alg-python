import pytest

from src.n901 import StockSpanner, StockSpannerA
from tests.case_loader import Case, load_cases


@pytest.fixture(params=[StockSpannerA])
def stock_spanner_cls(request: pytest.FixtureRequest) -> type[StockSpanner]:
    return request.param


@pytest.mark.parametrize("case", load_cases(__file__))
def test_stock_spanner(stock_spanner_cls: type[StockSpanner], case: Case):
    stock_spanner = stock_spanner_cls(*case["init"])
    actual = [
        getattr(stock_spanner, operation)(*arguments)
        for operation, arguments in zip(case["operations"], case["arguments"])
    ]
    assert actual == case["expected"]
