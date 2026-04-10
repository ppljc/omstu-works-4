from typing import List, Tuple

FACE_NAMES = ["front", "back", "left", "right", "top", "bottom"]
OPPOSITE = [1, 0, 3, 2, 5, 4]


def read_input(path: str = "task9_4.txt") -> str:
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return ""


def solve(data: str) -> str:
    nums = list(map(int, data.split()))
    p = 0
    case_no = 1
    blocks = []

    while p < len(nums):
        n = nums[p]
        p += 1
        if n == 0:
            break

        cubes = []
        for _ in range(n):
            cubes.append(nums[p:p + 6])
            p += 6

        # Для каждого цвета верхней грани храним лучший уже обработанный state
        best_state_by_color = [-1] * 101

        # Хранилище всех состояний:
        # length[s]  - длина башни, заканчивающейся этим состоянием
        # prev[s]    - предыдущий state
        # cube_id[s] - номер кубика во входе
        # face_id[s] - какая грань была сверху
        # top_color[s] - цвет верхней грани
        length: List[int] = []
        prev: List[int] = []
        cube_id: List[int] = []
        face_id: List[int] = []
        top_color: List[int] = []

        best_overall = -1

        for i, colors in enumerate(cubes, start=1):
            current_states = []

            # Пробуем поставить кубик i каждой из 6 граней вверх
            for f in range(6):
                top_c = colors[f]
                bottom_c = colors[OPPOSITE[f]]

                prev_state = best_state_by_color[bottom_c]
                cur_len = (length[prev_state] if prev_state != -1 else 0) + 1

                sid = len(length)
                length.append(cur_len)
                prev.append(prev_state)
                cube_id.append(i)
                face_id.append(f)
                top_color.append(top_c)

                current_states.append(sid)

                if best_overall == -1 or cur_len > length[best_overall]:
                    best_overall = sid

            # После обработки кубика обновляем лучшие состояния по цветам
            for sid in current_states:
                c = top_color[sid]
                if best_state_by_color[c] == -1 or length[sid] > length[best_state_by_color[c]]:
                    best_state_by_color[c] = sid

        # Восстановление ответа
        answer: List[Tuple[int, str]] = []
        s = best_overall
        while s != -1:
            answer.append((cube_id[s], FACE_NAMES[face_id[s]]))
            s = prev[s]
        answer.reverse()

        block = [f"Case #{case_no}", str(len(answer))]
        block.extend(f"{idx} {face}" for idx, face in answer)
        blocks.append("\n".join(block))

        case_no += 1

    return "\n\n".join(blocks)


if __name__ == "__main__":
    print(solve(read_input()))