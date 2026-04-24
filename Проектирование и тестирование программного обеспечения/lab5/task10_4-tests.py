import pytest
from task10_4 import solve_task_setter

@pytest.mark.parametrize("nk, np, categories_needed, task_to_cats, expected_status", [
    (
        3, 15, [3, 3, 4],
        [[1, 2], [3], [3], [3], [3], [1, 2, 3], [2, 3], [1, 3], [2], [2], [1, 2], [1, 3], [1, 2], [1], [1, 2, 3]],
        1
    ),
    (
        3, 15, [7, 3, 4],
        [[1, 2], [1], [2], [2], [3], [1, 2, 3], [2, 3], [2], [2], [2, 3], [2, 3], [1, 2], [1], [1, 2, 3]],
        0
    ),
    # Тест 1: Простейший успешный случай
    (
            2, 3, [1, 1],
            [[1], [2], [1, 2]],
            1
    ),
    # Тест 2: Задач достаточно, но они не подходят под категории (провал)
    (
            2, 2, [1, 1],
            [[1], [1]],
            0
    ),
    # Тест 3: Одна задача может закрыть одну из двух категорий (выбор пути)
    (
            2, 2, [1, 1],
            [[1, 2], [2]],
            1
    ),
    # Тест 4: Суммарно задач меньше, чем требует условие (провал)
    (
            3, 2, [1, 1, 1],
            [[1, 2, 3], [1, 2, 3]],
            0
    ),
    # Тест 5: Большой тест, где задачи сильно пересекаются
    (
            3, 5, [2, 1, 2],
            [[1], [1, 2], [2, 3], [1, 3], [3]],
            1
    )
])
def test_solve_task_setter_status(nk, np, categories_needed, task_to_cats, expected_status):
    status, result = solve_task_setter(nk, np, categories_needed, task_to_cats)
    assert status == expected_status

    if status == 1:
        assert len(result) == nk
        used_tasks = set()
        for i, tasks in enumerate(result):
            assert len(tasks) == categories_needed[i]
            for t in tasks:
                assert t not in used_tasks
                assert (i + 1) in task_to_cats[t - 1]
                used_tasks.add(t)