def task4_4() -> None:
    stack = [3, 1, 2, 5, 4]
    pancake = 0

    for i in range(len(stack)):
        pancake, pancake_index = find_next_max(stack, pancake)
        if pancake == current_max:
            stack = flip(stack, i)

            flip_pancake_index = find_where_flip(stack, pancake)

            stack = flip(stack, flip_pancake_index)

            current_max = find_next_max(stack, current_max)

            print(stack)


def blocks_input() -> list[list]:
    """
    Function to enter input blocks
    :return: List with blocks
    """
    blocks = []

    while True:
        stack = input()

        if stack == '':
            break

        blocks.append([int(i) for i in stack.split(' ')])

    return blocks


def find_next_max(stack: list, current_max: int) -> int:
    if current_max == 0:
        return max(stack)

    copy_stack = stack.copy()
    for i in range(len(stack)):
        pancake = stack[i]
        if pancake >= current_max:
            copy_stack.remove(pancake)

    new_max = max(copy_stack)
    return new_max


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
