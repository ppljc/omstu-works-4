import pytest
from task2_4 import *


@pytest.fixture
def standard_deck():
    return list(range(52))


@pytest.mark.parametrize("combination, expected_top_cards, description", [
    # 1. Identity permutation (Ничего не меняется)
    (
            list(range(52)),
            [0, 1, 2, 3],
            "No changes: combination is 1, 2, 3..."
    ),

    # 2. Swap first two (Меняем местами первые две карты)
    (
            [1, 0] + list(range(2, 52)),
            [1, 0, 2, 3],
            "Swap first two: 1 2 -> 2 1"
    ),

    # 3. Simple shift (Первая карта уходит в конец, остальные сдвигаются)
    (
            list(range(1, 52)) + [0],
            [1, 2, 3, 4],
            "Cycle shift: first card moves to the end"
    ),

    # 4. Reverse (Полный переворот колоды)
    (
            list(range(51, -1, -1)),
            [51, 50, 49, 48],
            "Full reverse: last becomes first"
    ),

    # 5. Mirror swap at the end (Меняем только две последние карты)
    (
            list(range(0, 50)) + [51, 50],
            [0, 1, 2, 3],  # начало не меняется
            "Swap last two cards"
    )
])
def test_process_deck(standard_deck, combination, expected_top_cards, description):
    result_deck = process_deck(standard_deck, combination)

    # Проверяем первые 4 карты для краткости, либо всю колоду, если нужно
    assert result_deck[:4] == expected_top_cards

    # В случае теста 5 (замена в конце), проверим еще и хвост
    if "last two" in description:
        assert result_deck[-2:] == [51, 50]


@pytest.mark.parametrize("combinations, tricks, expected_indices", [
    # Тест 1: Две комбинации, выполняется вторая (смена последних двух карт)
    (
            [
                [1, 0] + list(range(2, 52)),  # c0: меняет 1 и 2 местами
                list(range(0, 50)) + [51, 50]  # c1: меняет 51 и 52 местами
            ],
            [1],  # Выполняем только вторую комбинацию
            list(range(0, 50)) + [51, 50]
    ),

    # Тест 2: Одна комбинация, сдвиг первой карты в конец (циклический сдвиг влево)
    (
            [
                list(range(1, 52)) + [0]  # 52 карта становится на 1 место и т.д.
            ],
            [0],
            list(range(1, 52)) + [0]
    ),

    # Тест 3: Последовательное применение 3-х разных "трюков"
    (
            [
                [1, 0] + list(range(2, 52)),  # c0: меняет местами карты 0 и 1
                list(range(0, 46)) + [47, 46] + list(range(48, 52)),  # c1: меняет 46 и 47
                list(range(0, 47)) + [48, 47] + list(range(49, 52))  # c2: меняет 47 и 48
            ],
            [0, 1, 2],  # Выполняем 1, потом 2, потом 3
            [1, 0] + list(range(2, 46)) + [47, 48, 46] + list(range(49, 52))
    ),

    # Тест 4: Повторяющиеся трюки (1, 2, 1)
    (
            [
                list(range(0, 52)),  # c0: ничего не меняет (identity)
                [1, 0] + list(range(2, 52))  # c1: меняет первые две
            ],
            [0, 1, 0],  # Сначала ничего, потом замена, потом снова ничего
            [1, 0] + list(range(2, 52))
    ),

    # Тест 5: Полный реверс колоды
    (
            [
                list(range(51, -1, -1))  # От 51 до 0
            ],
            [0],
            list(range(51, -1, -1))
    )
])
def test_calculate(combinations, tricks, expected_indices):
    result = calculate(combinations, tricks)
    assert result == expected_indices