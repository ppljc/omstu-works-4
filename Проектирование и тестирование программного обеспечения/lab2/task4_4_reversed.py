def task4_4() -> None:
    print('Входные данные:')
    blocks = blocks_input()

    print('Выходные данные:')
    for stack in blocks:
        sorted_stack, flips = sort_stack(stack)

        flips = [str(abs(i - 5)) for i in flips]
        stack = [str(i) for i in stack]

        print(f"{str.join(' ', stack)}{' ' if flips else ''}{str.join(' ', flips)} 0")


def sort_stack(stack: list) -> tuple[list, list]:
    def ready():
        if stack == sorted_stack:
            # print("STOP")
            return True
        else:
            # print("DONT STOP BABY")
            return False

    flips = []
    sorted_stack = stack.copy()
    sorted_stack.sort(reverse=False)
    current_max = 0

    while True:
        # print('START')
        # print(f"stack before={stack}, sorted stack={sorted_stack}")

        if ready(): break

        current, prev_current_max_index = find_next_max(stack, current_max)  # find next max
        current_max, current_max_index = current
        # print(f"prev_current_max_index={prev_current_max_index}")
        # print(f"current_max={current_max}, current_max_index={current_max_index}")

        if prev_current_max_index == current_max_index + 1:
            # print("WE ARE GOING IF WAY")

            current_max -= 1
        else:
            # print("WE ARE GOING ELSE WAY")

            if not current_max_index == 0:
                # print("NEED THIS")
                stack = flip(stack, current_max_index)
                # print(f"stack after 1={stack}")
                flips.append(current_max_index)

                if ready(): break

        flip_pancake_index = find_where_flip(stack, current_max)
        # print(f"flip_pancake_index={flip_pancake_index}")

        stack = flip(stack, flip_pancake_index)
        flips.append(flip_pancake_index)
        # print(f"stack after 2={stack}")
        # print('END')

        if ready(): break

    return stack, flips


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


def find_next_max(stack: list, current_max: int) -> tuple[tuple[int, int], int]:
    previous_max = -1

    if current_max == 0:
        return find_max(stack), previous_max

    copy_stack = stack.copy()
    for i in range(len(stack)):
        pancake = stack[i]
        if pancake == current_max:
            previous_max = i
        if pancake >= current_max:
            copy_stack[i] = -1

    return find_max(copy_stack), previous_max


def find_max(stack: list) -> tuple[int, int]:
    current_max = max(stack)

    for i in range(len(stack)):
        if current_max == stack[i]:
            return current_max, i


def find_where_flip(stack: list, current_max: int):
    # print('find_where_flip')
    for i in range(len(stack)):
        pancake = stack[i]
        # print(f"pancake={pancake}")
        if pancake == current_max + 1:
            # print(f"pancake higher than {current_max} is {pancake} with index {i}")
            if i - 1 >= 0:
                # print(f"flip needed from {i - 1}")
                return i - 1
            else:
                return 0
    return len(stack) - 1


def flip(stack: list, pancake_index: int):
    copy_stack = stack.copy()
    copy_stack = copy_stack[:pancake_index + 1]
    copy_stack.reverse()
    return copy_stack + stack[pancake_index + 1:]


if __name__ == '__main__':
    task4_4()
