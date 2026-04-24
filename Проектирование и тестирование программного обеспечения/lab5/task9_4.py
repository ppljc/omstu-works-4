OPPOSITE = [1, 0, 3, 2, 5, 4]
FACE_NAMES = ["front", "back", "left", "right", "top", "bottom"]


def solve_tower(n, cubes):
    dp = [[1] * 6 for _ in range(n)]
    parent = [[None] * 6 for _ in range(n)]

    for i in range(n - 1, -1, -1):
        for f in range(6):
            bottom_color_i = cubes[i][OPPOSITE[f]]

            for j in range(i + 1, n):
                for f_below in range(6):
                    if cubes[j][f_below] == bottom_color_i:
                        if 1 + dp[j][f_below] > dp[i][f]:
                            dp[i][f] = 1 + dp[j][f_below]
                            parent[i][f] = (j, f_below)

    max_h = 0
    start_node = None
    for i in range(n):
        for f in range(6):
            if dp[i][f] > max_h:
                max_h = dp[i][f]
                start_node = (i, f)

    tower_result = []
    curr = start_node
    while curr:
        idx, f_idx = curr
        tower_result.append((idx + 1, FACE_NAMES[f_idx]))
        curr = parent[idx][f_idx]

    return max_h, tower_result


def main():
    input_file = 'task9_4.txt'

    try:
        with open(input_file, 'r') as f:
            data = f.read().split()
    except FileNotFoundError:
        return

    if not data:
        return

    ptr = 0
    case_num = 1

    while ptr < len(data):
        n = int(data[ptr])
        ptr += 1

        if n == 0:
            break

        cubes = []
        for _ in range(n):
            faces = [int(x) for x in data[ptr: ptr + 6]]
            cubes.append(faces)
            ptr += 6

        max_height, tower = solve_tower(n, cubes)

        if case_num > 1:
            print()  # Пустая строка между блоками

        print(f"Case #{case_num}")
        print(max_height)
        for cube_id, face_name in tower:
            print(f"{cube_id} {face_name}")

        case_num += 1


if __name__ == "__main__":
    main()
