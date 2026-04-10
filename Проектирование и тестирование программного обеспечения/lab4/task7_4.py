def task7_4() -> None:
    print('Входные данные:')
    blocks = blocks_input()

    print('Выходные данные:')
    for block in blocks:
        smaller, larger = find_closest_team_sums(block)
        print(f"{smaller} {larger}")

        print()


def blocks_input(file_path: str = "task7_4.txt") -> list:
    """
    Function to read input blocks from a file
    :param file_path: Path to the input file
    :return: List with blocks
    """
    blocks = []

    with open(file_path, 'r', encoding='utf-8') as f:
        lines = (line.strip() for line in f)

        try:
            line = next(lines)
            while not line:
                line = next(lines)
            blocks_amount = int(line)

            try:
                next(lines)
            except StopIteration:
                pass

            for _ in range(blocks_amount):
                n_line = next(lines)
                while not n_line:
                    n_line = next(lines)

                weights = []

                n = int(n_line)
                for i in range(n):
                    weight = next(lines)
                    weights.append(int(weight))

                blocks.append(weights)

        except StopIteration:
            pass

    return blocks


def find_closest_team_sums(weights: list[int]) -> tuple[int, int]:
    n = len(weights)
    if n == 0:
        return 0, 0

    k = n // 2
    total = sum(weights)

    possible_sums: list[set[int]] = [set() for _ in range(k + 1)]
    possible_sums[0].add(0)

    for weight in weights:
        for j in range(k, 0, -1):
            new_sums = {s + weight for s in possible_sums[j - 1]}
            possible_sums[j].update(new_sums)

    best_sum = min(
        possible_sums[k],
        key=lambda s: abs(2 * s - total)
    )

    sum_a = best_sum
    sum_b = total - best_sum

    return min(sum_a, sum_b), max(sum_a, sum_b)


if __name__ == "__main__":
    task7_4()
