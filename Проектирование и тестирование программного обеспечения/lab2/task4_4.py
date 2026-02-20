def task4_4() -> None:
    pass


def blocks_input() -> list[list]:
    """
    Function to enter input blocks
    :return: List with blocks
    """
    blocks = []

    while True:
        word = input()

        if word == '':
            break

        blocks.append([int(i) for i in word.split(' ')])

    return blocks


def flip(stack: list, pancake: int):
    pass
