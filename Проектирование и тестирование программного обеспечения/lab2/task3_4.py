def task3_4() -> None:
    """
    Function to find matching letters in two words
    :return: None
    """
    print('Входные данные:')
    blocks = blocks_input()

    print('Выходные данные:')
    for block in blocks:
        word_a, word_b = block

        substring = found_matching_substring(word_a, word_b)

        print(substring)


def blocks_input(file_path: str = "task3_4.txt") -> list[list]:
    """
    Function to enter input blocks
    :param file_path: Path to the input file
    :return: List with blocks
    """
    blocks = []
    block = []

    with open(file_path, 'r', encoding='utf-8') as f:
        lines = (line.strip() for line in f)

        try:
            while True:
                try:
                    if len(block) == 2:
                        blocks.append(tuple(block))
                        block = []

                    word = next(lines)

                    if word == '':
                        break

                    block.append(word)
                except StopIteration:
                    break
        except StopIteration:
            pass

    return blocks


def found_matching_substring(word_a: str, word_b: str) -> str:
    """
    Find matching letters in two words
    :param word_a: First word
    :param word_b: Second word
    :return: Matching letters
    """
    result = ''  # matching letters

    for letter in word_a:  # for letter in first word
        if letter in word_b and not(word_a.count(letter) == word_b.count(letter) == result.count(letter)):  # if letter from first word in second word and not in matching letters
            result += letter * min(word_a.count(letter), word_b.count(letter))  # add to matching letters all entering of current letter

    return result


if __name__ == '__main__':
    task3_4()
