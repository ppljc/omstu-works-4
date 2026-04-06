import math


def task5_4() -> None:
    """
    Function to find power of 2
    :return: None
    """
    print('Входные данные:')
    blocks = blocks_input()

    print('Выходные данные:')
    for number in blocks:
        result = calculate(number)

        print(result)


def blocks_input(file_path: str = "task5_4.txt") -> list[int]:
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
                    number = next(lines)

                    if number == '':
                        break

                    blocks.append(int(number))
                except StopIteration:
                    break
        except StopIteration:
            pass

    return blocks


def calculate(number: int) -> int | str:
    """
    Function to determine power of 2 which startswith given number
    :param number: Decimal
    :return: Power of 2 or string 'no power of 2'
    """
    start_digits = len(str(number)) + 1

    while start_digits < 11:
        new_number = int(str(number) + ("0" * start_digits))

        power = math.log2(new_number)

        low_border = math.floor(power)
        low_number_str = str(pow(2, low_border))
        high_border = math.ceil(power)
        high_number_str = str(pow(2, high_border))

        if low_number_str.startswith(str(number)):
            if len(low_number_str) >= start_digits:
                print(low_number_str)
                return low_border
        elif high_number_str.startswith(str(number)):
            if len(high_number_str) >= start_digits:
                print(high_number_str)
                return high_border

        start_digits += 1

    return "no power of 2"


if __name__ == '__main__':
    task5_4()
