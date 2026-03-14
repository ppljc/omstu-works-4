import pytest
from task5_4 import *


@pytest.mark.parametrize("number, expected", [
    (1, 7),
    (2, 8),
    (10, 20),
    (52, 19),
    (42, 32)
])
def test_found_matching_substring(number, expected):
    assert calculate(number) == expected
