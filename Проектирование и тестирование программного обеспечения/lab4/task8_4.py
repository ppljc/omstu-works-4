def task8_4():
    print('Входные данные')
    blocks = blocks_input()

    print('Выходные данные:')
    for idx, (A, cuts) in enumerate(blocks, 1):
        if not all(0 < c < A for c in cuts) or cuts != sorted(cuts):
            print(f"Некорректные данные в блоке {idx}. Пропускаем.")
            continue

        cost = min_cut_cost(A, cuts)
        print(f"The minimum cutting price is {cost}.")


def blocks_input(file_path: str = "task8_4.txt") -> list:
    blocks = []
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = [line.strip() for line in f if line.strip()]  # Убираем пустые строки

        i = 0
        while i < len(lines):
            A = int(lines[i])
            if A == 0:
                break
            i += 1
            if i >= len(lines):
                break
            B = int(lines[i])
            i += 1
            if i + B > len(lines):
                break
            cuts = list(map(int, lines[i:i + B]))
            blocks.append((A, cuts))
            i += B
    except FileNotFoundError:
        print(f"Файл {file_path} не найден. Используйте правильный путь.")
    except Exception as e:
        print(f"Ошибка чтения файла: {e}")
    return blocks


def min_cut_cost(length: int, cuts: list[int]) -> int:
    """
    Вычисляет минимальную стоимость распила бруса длиной length в позициях cuts.

    :param length: длина бруса
    :param cuts: список позиций распилов (строго возрастающий, 0 < Ci < length)
    :return: минимальная суммарная стоимость
    """
    if not cuts:
        return 0

    points = [0] + cuts + [length]
    n = len(points)

    dp = [[0] * n for _ in range(n)]

    for interval_len in range(2, n):
        for left in range(n - interval_len):
            right = left + interval_len
            seg_len = points[right] - points[left]

            min_cost = float('inf')
            for k in range(left + 1, right):
                cost = dp[left][k] + dp[k][right] + seg_len
                if cost < min_cost:
                    min_cost = cost

            dp[left][right] = min_cost

    return dp[0][n - 1]


if __name__ == "__main__":
    task8_4()