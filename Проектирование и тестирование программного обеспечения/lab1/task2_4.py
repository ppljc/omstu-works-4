def task2_4() -> None:
    """
    Function to calculate cards desk after given tricks
    :return: None
    """
    print('Входные данные:')
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


def blocks_input() -> list:
    """
    Function to enter input blocks
    :return: List with blocks
    """
    blocks_amount = int(input())  # blocks amount
    _space = input()  # space
    blocks = []

    for _block in range(blocks_amount):
        n = int(input())  # combinations amount
        combinations = []  # list of combinations where was a trick

        for i in range(n):  # combinations enter
            combination = input()
            combinations.append([int(i) - 1 for i in combination.split(' ')])  # turn card numbers to massive indexes (i - 1)

        tricks = []  # order of tricks indexes

        while True:
            trick_index = input()
            if trick_index == '':  # on blank line - stop entering
                break

            tricks.append(int(trick_index) - 1)  # turn trick indexes to massive indexes (i - 1)

        blocks.append((combinations, tricks))

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
