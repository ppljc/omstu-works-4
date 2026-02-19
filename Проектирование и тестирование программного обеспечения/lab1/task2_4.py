default_deck = [i for i in range(52)]  # default desk for tricks processing


def string_input() -> list:
    print('Входные данные:')
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


def task2_4():
    desk = [i for i in range(52)]  # default desk

    blocks = string_input()

    print('Выходные данные:')
    for block in blocks:
        combinations, tricks_indexes = block
        tricks = []

        for combination in combinations:
            tricks.append(process_combination(combination))  # from every combination (with trick) get a trick

        for trick_index in tricks_indexes:
            desk = process_deck(desk, tricks[trick_index])

        for card in desk:
            print(get_card_name(card))


def process_combination(combination: list) -> dict:
    """
    Get trick indexes from desk combination
    :param combination: List with shuffled desk with indexes of 52 elements
    :return: Dictionary {to move index: will be moved index, ...}
    """
    combination_deck = {}  # dictionary with tricks, where which card (by index) should be moved

    for i in range(52):
        if default_deck[i] != combination[i] and not combination_deck.get(combination[i]):  # if default card not equal card in combination with same index and this trick not already in dict
            combination_deck[default_deck[i]] = combination[i]  # add trick in format of indexes |to move: will be moved|

    return combination_deck


def process_deck(desk: list, trick: dict) -> list:
    """
    Process desk according to trick
    :param desk: List of cards with indexes of 52 elements
    :param trick: Dictionary {to move index: will be moved index, ...}
    :return: List of cards with indexes of 52 elements which were shuffled according to trick
    """
    for to_move, will_be_moved in trick.items():
        temp = desk[to_move]
        desk[to_move] = desk[will_be_moved]
        desk[will_be_moved] = temp

    return desk


def get_card_name(index: int):
    string_builder = []

    card_number = index - (index // 13) * 13
    if card_number < 9:
        string_builder.append(str(card_number + 2))
    match card_number:
        case 9:
            string_builder.append("Jack")
        case 10:
            string_builder.append("Queen")
        case 11:
            string_builder.append("King")
        case 12:
            string_builder.append("Ace")

    string_builder.append("of")

    if 0 <= index <= 12:
        string_builder.append('Clubs')
    elif 13 <= index <= 25:
        string_builder.append('Diamonds')
    elif 26 <= index <= 38:
        string_builder.append('Hearts')
    elif 39 <= index <= 51:
        string_builder.append('Spades')

    return " ".join(string_builder)


if __name__ == '__main__':
    task2_4()
