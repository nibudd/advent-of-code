import pytest

from algorithms.max_frequency_deviation import max_frequency_deviation


@pytest.mark.parametrize("input,expected", [
    ("a", 0),
    ("aaa", 0),
    ("aabb", 1),
    ("aabcccacb", 3)
])
def test_returns_expected_result(input: str, expected: int):
    result = max_frequency_deviation(input)
    assert result == expected
