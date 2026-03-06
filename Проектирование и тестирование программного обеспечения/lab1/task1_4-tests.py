import pytest
import copy
from task1_4 import *


@pytest.mark.parametrize("votes, expected", [
    # Тест 1: Обычный случай (один явный аутсайдер)
    (
        {
            'John': {'votes': 10, 'index': 0},
            'Jane': {'votes': 5, 'index': 1},
            'Bob': {'votes': 7, 'index': 2}
        },
        ('Jane', {'votes': 5, 'index': 1})
    ),

    # Тест 2: Ничья (несколько кандидатов с минимальным баллом)
    (
        {
            'John': {'votes': 5, 'index': 0},
            'Jane': {'votes': 10, 'index': 1},
            'Bob': {'votes': 5, 'index': 2}
        },
        ('Bob', {'votes': 5, 'index': 2})
    ),

    # Тест 3: Граничный случай (всего один кандидат)
    (
        {'Solo': {'votes': 100, 'index': 0}},
        ('Solo', {'votes': 100, 'index': 0})
    ),

    # Тест 4: Нулевые значения (кандидат вообще без голосов)
    (
        {
            'Active': {'votes': 1, 'index': 0},
            'Zero': {'votes': 0, 'index': 1}
        },
        ('Zero', {'votes': 0, 'index': 1})
    ),

    # Тест 5: Все кандидаты имеют одинаковое количество голосов
    (
        {
            'A': {'votes': 3, 'index': 0},
            'B': {'votes': 3, 'index': 1},
            'C': {'votes': 3, 'index': 2}
        },
        ('C', {'votes': 3, 'index': 2})
    )
])
def test_get_lowest_candidate(votes: dict, expected: tuple):
    assert get_lowest_candidate(votes) == expected


@pytest.mark.parametrize("votes, expected", [
    # Тест 1: Обычный случай (один явный лидер)
    (
        {
            'John': {'votes': 5, 'index': 0},
            'Jane': {'votes': 15, 'index': 1},
            'Bob': {'votes': 7, 'index': 2}
        },
        ('Jane', {'votes': 15, 'index': 1})
    ),

    # Тест 2: Ничья (несколько лидеров)
    (
        {
            'John': {'votes': 12, 'index': 0},
            'Jane': {'votes': 12, 'index': 1},
            'Bob': {'votes': 12, 'index': 2}
        },
        ('Bob', {'votes': 12, 'index': 2})
    ),

    # Тест 3: Минимальный набор данных (один кандидат)
    (
        {'Solo': {'votes': 10, 'index': 0}},
        ('Solo', {'votes': 10, 'index': 0})
    ),

    # Тест 4: Нулевые голоса (все по нулям)
    (
        {
            'First': {'votes': 0, 'index': 0},
            'Second': {'votes': 0, 'index': 1},
            'Last': {'votes': 0, 'index': 2}
        },
        ('Last', {'votes': 0, 'index': 2})
    ),

    # Тест 5: Большие значения (проверка корректности сравнения при больших числах)
    (
        {
            'Candidate A': {'votes': 999999, 'index': 0},
            'Candidate B': {'votes': 1000000, 'index': 1}
        },
        ('Candidate B', {'votes': 1000000, 'index': 1})
    )
])
def test_get_highest_candidate(votes, expected):
    assert get_highest_candidate(votes) == expected


@pytest.mark.parametrize("votes, expected", [
    # Тест 1: Один явный проигравший
    (
            {
                'A': {'votes': 10, 'index': 0},
                'B': {'votes': 2, 'index': 1},
                'C': {'votes': 10, 'index': 2}
            },
            (
                    {'A': {'votes': 10, 'index': 0}, 'C': {'votes': 10, 'index': 2}},  # Остались
                    {'B': {'votes': 2, 'index': 1}}  # Удален
            )
    ),

    # Тест 2: Несколько проигравших с одинаковым минимумом
    (
            {
                'Winner': {'votes': 15, 'index': 0},
                'Loser1': {'votes': 3, 'index': 1},
                'Loser2': {'votes': 3, 'index': 2}
            },
            (
                    {'Winner': {'votes': 15, 'index': 0}},
                    {'Loser1': {'votes': 3, 'index': 1}, 'Loser2': {'votes': 3, 'index': 2}}
            )
    ),

    # Тест 3: Все кандидаты имеют равное количество голосов
    (
            {
                'A': {'votes': 5, 'index': 0},
                'B': {'votes': 5, 'index': 1}
            },
            (
                    {},
                    {'A': {'votes': 5, 'index': 0}, 'B': {'votes': 5, 'index': 1}}
            )
    ),

    # Тест 4: Только один кандидат в списке
    (
            {'Solo': {'votes': 10, 'index': 0}},
            (
                    {},
                    {'Solo': {'votes': 10, 'index': 0}}
            )
    ),

    # Тест 5: Проигравший с нулевым результатом
    (
            {
                'A': {'votes': 0, 'index': 0},
                'B': {'votes': 1, 'index': 1}
            },
            (
                    {'B': {'votes': 1, 'index': 1}},
                    {'A': {'votes': 0, 'index': 0}}
            )
    )
])
def test_remove_lowest_candidates(votes, expected):
    result_new, result_removed = remove_lowest_candidates(votes)
    expected_new, expected_removed = expected

    assert result_new == expected_new
    assert result_removed == expected_removed


@pytest.mark.parametrize("votes, person, expected_votes, expected_person", [
    # Тест 1: Голос переходит ко второму кандидату в списке
    (
            {'Jane': {'votes': 5, 'index': 1}, 'Bob': {'votes': 2, 'index': 2}},  # Активные
            [0, 1, 2],  # 0-й выбыл, ищем следующего. 1-й (Jane) активен.
            {'Jane': {'votes': 6, 'index': 1}, 'Bob': {'votes': 2, 'index': 2}},  # Jane получила +1
            [1, 2]  # Новый список предпочтений начинается с Jane
    ),

    # Тест 2: Голос переходит через одного (второй тоже выбыл)
    (
            {'Bob': {'votes': 10, 'index': 2}},  # Только Bob активен
            [0, 1, 2],  # 0 и 1 выбыли
            {'Bob': {'votes': 11, 'index': 2}},
            [2]
    ),

    # Тест 3: Никого из списка избирателя нет в активных голосах
    (
            {'Alice': {'votes': 5, 'index': 3}},  # Активна только Alice (индекс 3)
            [0, 1, 2],  # В бюллетене только 0, 1, 2
            {'Alice': {'votes': 5, 'index': 3}},  # Голоса не изменились
            []  # Список пуст
    ),

    # Тест 4: Список избирателя состоит только из одного (выбывшего) кандидата
    (
            {'Jane': {'votes': 5, 'index': 1}},
            [0],  # Тот, кто был под индексом 0, выбыл
            {'Jane': {'votes': 5, 'index': 1}},
            []
    ),

    # Тест 5: Голос переходит кандидату, у которого было 0 голосов
    (
            {'C': {'votes': 0, 'index': 2}},
            [0, 2],
            {'C': {'votes': 1, 'index': 2}},
            [2]
    )
])
def test_get_new_person_vote(votes, person, expected_votes, expected_person):
    current_votes = copy.deepcopy(votes)

    res_votes, res_person = get_new_person_vote(current_votes, person)

    assert res_votes == expected_votes
    assert res_person == expected_person


@pytest.mark.parametrize("votes, expected", [
    # Тест 1: Идеальное равенство (все имеют одинаковый балл)
    (
        {
            'Alice': {'votes': 5, 'index': 0},
            'Bob': {'votes': 5, 'index': 1},
            'Charlie': {'votes': 5, 'index': 2}
        },
        ['Alice', 'Bob', 'Charlie']
    ),

    # Тест 2: Голоса не равны (есть лидер)
    (
        {
            'Alice': {'votes': 6, 'index': 0},
            'Bob': {'votes': 5, 'index': 1}
        },
        [] # Должен вернуть пустой список, так как есть разница
    ),

    # Тест 3: Граничный случай (один кандидат)
    # Один всегда равен самому себе — это ситуация автоматической победы
    (
        {'Solo': {'votes': 10, 'index': 0}},
        ['Solo']
    ),

    # Тест 4: Равенство при нуле голосов
    (
        {
            'A': {'votes': 0, 'index': 0},
            'B': {'votes': 0, 'index': 1}
        },
        ['A', 'B']
    ),

    # Тест 5: Почти равенство (разница в один голос)
    (
        {
            'Candidate 1': {'votes': 100, 'index': 0},
            'Candidate 2': {'votes': 100, 'index': 1},
            'Candidate 3': {'votes': 101, 'index': 2}
        },
        []
    )
])
def test_check_votes_equal(votes, expected):
    result = check_votes_equal(votes)
    assert sorted(result) == sorted(expected)


@pytest.mark.parametrize("people, votes, expected", [
    # Тест 1: Ваш кейс (John Doe побеждает после перераспределения)
    # Кандидаты: 0: John Doe, 1: Jane Smith, 2: Jane Austen
    (
        [
            [0, 1, 2], # 1 2 3
            [1, 0, 2], # 2 1 3
            [1, 2, 0], # 2 3 1
            [0, 1, 2], # 1 2 3
            [2, 0, 1]  # 3 1 2
        ],
        {
            'John Doe': {'votes': 2, 'index': 0},
            'Jane Smith': {'votes': 2, 'index': 1},
            'Jane Austen': {'votes': 1, 'index': 2}
        },
        ['John Doe']
    ),

    # Тест 2: Победа сразу (абсолютное большинство > 50%)
    (
        [[0, 1], [0, 1], [0, 1]], # Все за первого
        {'A': {'votes': 3, 'index': 0}, 'B': {'votes': 0, 'index': 1}},
        ['A']
    ),

    # Тест 3: Ничья (все равны изначально)
    (
        [[0, 1], [1, 0]],
        {'A': {'votes': 1, 'index': 0}, 'B': {'votes': 1, 'index': 1}},
        ['A', 'B']
    ),

    # Тест 4: Перераспределение приводит к ничьей
    # Сначала выбывает C, его голос делает ситуацию между A и B равной
    (
        [[0, 1, 2], [1, 0, 2], [2, 0, 1]],
        {'A': {'votes': 1, 'index': 0}, 'B': {'votes': 1, 'index': 1}, 'C': {'votes': 1, 'index': 2}},
        ['A', 'B', 'C'] # check_votes_equal сработает сразу
    ),

    # Тест 5: Сложный случай (несколько кругов исключения)
    (
        [[0, 1, 2, 3], [1, 2, 3, 0], [2, 3, 0, 1], [0, 1, 2, 3]],
        {
            'A': {'votes': 2, 'index': 0},
            'B': {'votes': 1, 'index': 1},
            'C': {'votes': 1, 'index': 2},
            'D': {'votes': 0, 'index': 3}
        },
        ['A']
    )
])
def test_calculate_votes(people, votes, expected):
    res = calculate_votes(copy.deepcopy(people), copy.deepcopy(votes))
    assert sorted(res) == sorted(expected)
