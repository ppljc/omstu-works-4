import pytest
from task9_4 import solve_tower


@pytest.mark.parametrize("n, cubes, expected_height", [
    (
        10,
        [
            [1, 5, 10, 3, 6, 5],
            [2, 6, 7, 3, 6, 9],
            [5, 7, 3, 2, 1, 9],
            [1, 3, 3, 5, 8, 10],
            [6, 6, 2, 2, 4, 4],
            [1, 2, 3, 4, 5, 6],
            [10, 9, 8, 7, 6, 5],
            [6, 1, 2, 3, 4, 7],
            [1, 2, 3, 3, 2, 1],
            [3, 2, 1, 1, 2, 3]
        ],
        8
    ),
    (
        3,
        [
            [1, 2, 2, 2, 1, 2],
            [3, 3, 3, 3, 3, 3],
            [3, 2, 1, 1, 1, 1]
        ],
        2
    ),
    (
        1,
        [[1, 2, 3, 4, 5, 6]],
        1
    ),
    (
        2,
        [[1, 1, 1, 1, 1, 1], [2, 2, 2, 2, 2, 2]],
        1
    ),
    (
        2,
        [[5, 5, 5, 5, 1, 2], [2, 2, 2, 2, 2, 2]],
        2
    ),
    (
        3,
        [
            [10, 10, 10, 10, 1, 10],
            [20, 20, 20, 20, 10, 20],
            [20, 20, 20, 20, 20, 20]
        ],
        3
    )
])
def test_solve_tower_height(n, cubes, expected_height):
    height, tower = solve_tower(n, cubes)
    assert height == expected_height
    assert len(tower) == expected_height
