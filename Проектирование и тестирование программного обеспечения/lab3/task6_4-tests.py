import pytest
from task6_4 import *


@pytest.mark.parametrize(
    "max_m, max_d, m, k, expected",
    [
        # 1. Пустое выражение (m=0) всегда 1 при любом k
        (5, 5, 0, 0, 1),
        (5, 5, 0, 5, 1),
        # 2. m=1, k=0 → 0 (нельзя подняться)
        (5, 5, 1, 0, 0),
        # 3. m=1, k=1 → 1 (классическое "()")
        (5, 5, 1, 1, 1),
        # 4. m=3, k=2 → 4 (все выражения длины 6 с глубиной ≤2)
        (5, 5, 3, 2, 4),
    ],
)
def test_precompute_le(max_m, max_d, m, k, expected):
    le = precompute_le(max_m, max_d)
    assert le[m][k] == expected


@pytest.mark.parametrize(
    "max_m, max_d, m, d, expected",
    [
        # 1. m=0, d=0 → 1 (пустая строка)
        (5, 5, 0, 0, 1),
        # 2. m=1, d=1 → 1 ("()")
        (5, 5, 1, 1, 1),
        # 3. m=3, d=2 → 3 (пример из условия задачи)
        (5, 5, 3, 2, 3),
        # 4. m=3, d=3 → 1 (максимально вложенное)
        (5, 5, 3, 3, 1),
        # 5. m=4, d=3 → 5
        (5, 5, 4, 3, 5),
    ],
)
def test_precompute_exactly(max_m, max_d, m, d, expected):
    le = precompute_le(max_m, max_d)
    exactly = precompute_exactly(le, max_m, max_d)
    assert exactly[m][d] == expected


@pytest.mark.parametrize(
    "m, d, expected",
    [
        # 1. n=2, d=1
        (1, 1, 1),
        # 2. n=6, d=2 — пример из условия
        (3, 2, 3),
        # 3. n=6, d=3
        (3, 3, 1),
        # 4. n=8, d=2
        (4, 2, 7),
        # 5. n=10, d=3
        (5, 3, 18),
    ],
)
def test_precompute(m, d, expected):
    exactly = precompute()
    assert exactly[m][d] == expected


@pytest.mark.parametrize(
    "n, d, expected",
    [
        # 1. Классический пример из условия задачи
        (6, 2, 3),
        # 2. Максимальные значения из условия
        (300, 150, 1),
        # 3. Простой случай
        (4, 1, 1),
        # 4. Минимальный корректный случай
        (2, 1, 1),
        # 5. Максимально вложенное выражение длины 6
        (6, 3, 1),
    ],
)
def test_calculate(n, d, expected):
    """
    ТЕСТИРУЕМ ИМЕННО ФУНКЦИЮ calculate — основную логику всей программы
    (как и просил: вместо test_task6_4 теперь тестируем calculate)
    """
    exactly = precompute()
    result = calculate(n, d, exactly)
    assert result == expected