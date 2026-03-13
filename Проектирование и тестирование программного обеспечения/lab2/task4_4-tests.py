import pytest
from task4_4 import *


@pytest.mark.parametrize("stack, expected_flips", [
    (
        [1, 2, 3, 4, 5],
        []
    ),
    (
        [5, 4, 3, 2, 1],
        [1]
    ),
    (
        [5, 1, 2, 3, 4],
        [1, 2]
    ),
    (
        [1, 2, 4, 5, 3],
        [2, 1, 3, 4]
    ),
    (
        [5, 4, 3, 1, 2],
        [1, 4]
    )
])
def test_sort_stack(stack: list, expected_flips: list):
    sorted_stack, flips = sort_stack(stack)

    stack.sort()
    assert sorted_stack == stack
    assert flips == expected_flips
