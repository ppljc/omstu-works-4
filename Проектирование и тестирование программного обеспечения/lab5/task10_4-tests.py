import pytest

from task10_4 import min_cut_cost


@pytest.mark.parametrize(
    "length, cuts, expected",
    [
        # 1. Пример из условия
        (100, [25, 50, 75], 200),

        # 2. Второй пример из условия
        (10, [4, 5, 7, 8], 22),

        # 3. Нет распилов (крайний случай)
        (50, [], 0),

        # 4. Один распил
        (10, [5], 10),

        # 5. Несбалансированные распилы (проверка оптимальности порядка)
        (20, [2, 8, 10], 38),
    ]
)
def test_min_cut_cost(length, cuts, expected):
    assert min_cut_cost(length, cuts) == expected
