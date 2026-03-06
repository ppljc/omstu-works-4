import pytest
from task3_4 import *


@pytest.mark.parametrize("word_a, word_b, expected_substring", [
    (
        "pretty",
        "women",
        "e"
    ),
    (
        "walking",
        "down",
        "wn"
    ),
    (
        "the",
        "street",
        "te"
    ),
    (
        "milk",
        "klim",
        "milk"
    ),
    (
        "goner",
        "play",
        ""
    ),
    (
        " ",
        "a b",
        " "
    )
])
def test_found_matching_substring(word_a, word_b, expected_substring):
    substring = found_matching_substring(word_a, word_b)
    assert str(list(substring).sort()) == str(list(expected_substring).sort())
