def task3_4() -> None:
    pass


def blocks_input() -> list[list]:
    blocks = []
    block = []

    while True:
        if len(block) > 2:
            blocks.append(block)
            block = []

        word = input()

        if word == '':
            break

        block.append(word)

    return blocks


def found_substring():
    pass
