def task4_4() -> None:
    stack = [1, 2, 4, 3, 5]
    current_max = 0

    while stack != stack.sort():
        current_max, current_max_index = find_next_max(stack, current_max) # find next max

        stack = flip(stack, current_max_index)

        flip_pancake_index = find_where_flip(stack, current_max)

        stack = flip(stack, flip_pancake_index)

        print(stack)


def blocks_input(file_path: str = "task4_4.txt") -> list[list]:
    """
    Function to enter input blocks
    :return: List with blocks
    """
    blocks = []

    with open(file_path, 'r', encoding='utf-8') as f:
        lines = (line.strip() for line in f)

        try:
            while True:
                try:
                    stack = next(lines)

                    if stack == '':
                        break

                    blocks.append([int(i) for i in stack.split(' ')])
                except StopIteration:
                    break
        except StopIteration:
            pass

    return blocks


def find_next_max(stack: list, current_max: int) -> tuple[int, int]:
    if current_max == 0:
        return find_max(stack)

    copy_stack = stack.copy()
    for i in range(len(stack)):
        pancake = stack[i]
        if pancake >= current_max:
            copy_stack[i] = -1

    return find_max(copy_stack)


def find_max(stack: list) -> tuple[int, int]:
    current_max = max(stack)

    for i in range(len(stack)):
        if current_max == stack[i]:
            return current_max, i


def find_where_flip(stack: list, current_max: int):
    for i in range(len(stack)):
        pancake = stack[i]
        if pancake == current_max + 1:
            if i + 1 < len(stack):
                return i + 1
            else:
                return -1
        else:
            return 0


def flip(stack: list, pancake_index: int):
    copy_stack = stack.copy()
    copy_stack = copy_stack[pancake_index:]
    copy_stack.reverse()
    return stack[:pancake_index] + copy_stack


if __name__ == '__main__':
    task4_4()
