def task3_4() -> None:
    """
    Function to calculate Australian voting
    :return: None
    """
    print('Входные данные:')
    blocks = blocks_input()

    print('Выходные данные:')
    for block in blocks:
        word_a, word_b = block

        substring = found_matching_substring(word_a, word_b)

        print(substring)


def blocks_input() -> list[list]:
    blocks = []
    block = []

    while True:
        if len(block) == 2:
            blocks.append(tuple(block))
            block = []

        word = input()

        if word == '':
            break

        block.append(word)

    return blocks


def found_matching_substring(word_a: str, word_b: str) -> str:
    result = ''

    max_length = len(word_a)

    for start in range(0, max_length, 1):
        for length in range(1, max_length, 1):
            end = start + length

            if end > max_length:
                end = max_length

            substring = word_a[start:end]

            if substring in word_b and len(substring) >= len(result):
                result = substring

    return result


if __name__ == '__main__':
    task3_4()
