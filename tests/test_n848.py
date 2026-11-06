from pytest import fixture

from src.n848 import Solution, SolutionA, SolutionB


@fixture(scope='module', params=[SolutionA, SolutionB])
def solution(request) -> Solution:
    return request.param()


def test_a(solution: Solution):
    assert 'wqqwlcjnkphhsyvrkdod' == solution.shifting_letters(
        'mkgfzkkuxownxvfvxasy',
        [
            505870226,
            437526072,
            266740649,
            224336793,
            532917782,
            311122363,
            567754492,
            595798950,
            81520022,
            684110326,
            137742843,
            275267355,
            856903962,
            148291585,
            919054234,
            467541837,
            622939912,
            116899933,
            983296461,
            536563513,
        ],
    )


def test_b(solution: Solution):
    assert 'rpl' == solution.shifting_letters('abc', [3, 5, 9])


def test_c(solution: Solution):
    assert 'gfd' == solution.shifting_letters('aaa', [1, 2, 3])
