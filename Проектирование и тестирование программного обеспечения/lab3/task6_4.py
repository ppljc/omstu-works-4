import sys

MAX_N = 300


def precompute(max_n=MAX_N):
    """
    Предвычисляет таблицу:
    f[n][d] = число правильных скобочных последовательностей длины n
              с максимальной глубиной ≤ d
    """
    max_pairs = max_n // 2
    f = [[0] * (max_pairs + 2) for _ in range(max_n + 1)]

    for d in range(max_pairs + 1):
        dp = [[0] * (d + 2) for _ in range(max_n + 1)]
        dp[0][0] = 1

        for i in range(max_n):
            for bal in range(d + 1):
                cur = dp[i][bal]
                if cur == 0:
                    continue

                # добавить '('
                if bal + 1 <= d:
                    dp[i + 1][bal + 1] += cur

                # добавить ')'
                if bal > 0:
                    dp[i + 1][bal - 1] += cur

        for n in range(0, max_n + 1, 2):
            f[n][d] = dp[n][0]

    return f


def count_exact_depth(f, n, d):
    """
    Возвращает количество последовательностей длины n
    с глубиной ровно d
    """
    if n % 2 == 1:
        return 0

    pairs = n // 2
    d = min(d, pairs)

    if d == 0:
        return 0

    return f[n][d] - f[n][d - 1]


def solve():
    f = precompute()

    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue

        n, d = map(int, line.split())
        result = count_exact_depth(f, n, d)
        print(result)


if __name__ == "__main__":
    solve()