def task2_4() -> None:
    """
    Function to calculate cards desk after given tricks
    :return: None
    """
    print('Входные данные из файла')
    blocks = blocks_input()

    print('Выходные данные:')
    for block in blocks:
        combinations, tricks_indexes = block  # unpack block tuple

        desk = calculate(combinations, tricks_indexes)  # calculate one desk with given tricks

        for card in desk:  # output desk with card names
            print(get_card_name(card))
        print()


def calculate(combinations, tricks_indexes):
    desk = [i for i in range(len(combinations[0] if len(combinations) > 0 else 52))]  # default desk

    for trick_index in tricks_indexes:  # for every entered trick in order change desk
        desk = process_deck(desk, combinations[trick_index])  # process chosen trick to desk

    return desk


# def blocks_input() -> list:
#     """
#     Function to enter input blocks
#     :return: List with blocks
#     """
#     blocks_amount = int(input())  # blocks amount
#     _space = input()  # space
#     blocks = []
#
#     for _block in range(blocks_amount):
#         n = int(input())  # combinations amount
#         combinations = []  # list of combinations where was a trick
#
#         for i in range(n):  # combinations enter
#             combination = input()
#             combinations.append([int(i) - 1 for i in combination.split(' ')])  # turn card numbers to massive indexes (i - 1)
#
#         tricks = []  # order of tricks indexes
#
#         while True:
#             trick_index = input()
#             if trick_index == '':  # on blank line - stop entering
#                 break
#
#             tricks.append(int(trick_index) - 1)  # turn trick indexes to massive indexes (i - 1)
#
#         blocks.append((combinations, tricks))
#
#     return blocks


def blocks_input(file_path: str = "task2_4.txt") -> list:
    """
    Function to read input blocks from a file
    :param file_path: Path to the input file
    :return: List with blocks
    """
    blocks = []

    with open(file_path, 'r', encoding='utf-8') as f:
        # Создаем итератор, чтобы удобно брать строки по одной
        lines = (line.strip() for line in f)

        try:
            line = next(lines)
            if not line:  # Пропуск возможных начальных пустых строк
                line = next(lines)

            blocks_amount = int(line)

            for _ in range(blocks_amount):
                # Пропускаем пустую строку перед блоком, если она есть
                n_line = next(lines)
                while not n_line:
                    n_line = next(lines)

                n = int(n_line)
                combinations = []

                # Читаем N комбинаций
                for _ in range(n):
                    combination = next(lines)
                    combinations.append([int(i) - 1 for i in combination.split()])

                tricks = []
                # Читаем индексы трюков до следующей пустой строки или конца файла
                while True:
                    try:
                        trick_line = next(lines)
                        if trick_line == '':  # Пустая строка — признак конца блока трюков
                            break
                        tricks.append(int(trick_line) - 1)
                    except StopIteration:
                        break  # Конец файла

                blocks.append((combinations, tricks))

        except StopIteration:
            pass  # Файл закончился раньше ожидаемого

    return blocks


def process_deck(desk: list, combination: list) -> list:
    """
    Process desk according to trick
    :param desk: List of cards with indexes of 52 elements
    :param combination: List of cards with executed trick
    :return: List of cards with indexes of 52 elements which were shuffled according to trick
    """
    new_desk = [i for i in range(len(desk))]

    for i in range(len(combination)):
        new_desk[i] = desk[combination[i]]

    return new_desk


def get_card_name(index: int) -> str:
    """
    Get card name by index
    :param index: Index of card in desk
    :return: String with name of card
    """
    suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']

    suit = suits[index // 13]
    rank = ranks[index % 13]

    return f'{rank} of {suit}'


if __name__ == '__main__':
    task2_4()
