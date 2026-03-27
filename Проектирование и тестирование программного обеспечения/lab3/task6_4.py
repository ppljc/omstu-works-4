def task6_4():
    exactly = precompute()

    print('Входные данные:')
    blocks = blocks_input()

    print('Выходные данные:')
    for n, d in blocks:
        if n % 2 != 0 or n < 2 or n > 300:
            print(0)
            continue

        m = n // 2

        if m > 150 or d < 1 or d > 150:
            print(0)
            continue

        print(exactly[m][d])


def blocks_input(file_path: str = "task6_4.txt") -> list[list]:
    """
    Function to enter input blocks
    :param file_path: Path to the input file
    :return: List with blocks
    """
    blocks = []

    with open(file_path, 'r', encoding='utf-8') as f:
        lines = (line.strip() for line in f)

        try:
            while True:
                try:
                    numbers = next(lines)

                    if numbers == '':
                        break

                    numbers = [int(i) for i in numbers.split(' ')]

                    blocks.append(numbers)
                except StopIteration:
                    break
        except StopIteration:
            pass

    return blocks


def precompute_le(MAX_M: int, MAX_D: int):
    le = [[0] * (MAX_D + 1) for _ in range(MAX_M + 1)]

    for k in range(MAX_D + 1):
        le[0][k] = 1

        prev = [0] * (k + 1)
        prev[0] = 1

        for step in range(1, 2 * MAX_M + 1):
            curr = [0] * (k + 1)
            for j in range(k + 1):
                p = prev[j]
                if p == 0:
                    continue
                if j + 1 <= k:
                    curr[j + 1] += p
                if j - 1 >= 0:
                    curr[j - 1] += p
            prev = curr

            if step % 2 == 0:
                m = step // 2
                le[m][k] = prev[0]

    return le


def precompute_exactly(le: list, MAX_M: int, MAX_D: int):
    exactly = [[0] * (MAX_D + 1) for _ in range(MAX_M + 1)]

    for m in range(MAX_M + 1):
        exactly[m][0] = le[m][0]
        for d in range(1, MAX_D + 1):
            exactly[m][d] = le[m][d] - le[m][d - 1]

    return exactly


def precompute():
    MAX_M = 150
    MAX_D = 150
    le = precompute_le(MAX_M, MAX_D)
    exactly = precompute_exactly(le, MAX_M, MAX_D)
    return exactly


if __name__ == "__main__":
    task6_4()
