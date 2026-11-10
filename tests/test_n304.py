import pytest

from src.n304 import NumMatrix, NumMatrixA, NumMatrixB
from tests.case_loader import Case, load_cases


@pytest.fixture(params=[NumMatrixA, NumMatrixB])
def num_matrix_cls(request: pytest.FixtureRequest) -> type[NumMatrix]:
    return request.param


@pytest.mark.parametrize("case", load_cases(__file__))
def test_sum_region(num_matrix_cls: type[NumMatrix], case: Case):
    num_matrix = num_matrix_cls(*case["init"])
    actual = [
        getattr(num_matrix, operation)(*arguments)
        for operation, arguments in zip(case["operations"], case["arguments"])
    ]
    assert actual == case["expected"]
