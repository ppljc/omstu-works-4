def min_cut_cost(length, cuts):
    cuts = [0] + cuts + [length]
    n = len(cuts)

    dp = [[0] * n for _ in range(n)]

    for l in range(2, n):
        for i in range(n - l):
            j = i + l
            dp[i][j] = float('inf')

            for k in range(i + 1, j):
                cost = dp[i][k] + dp[k][j] + (cuts[j] - cuts[i])
                dp[i][j] = min(dp[i][j], cost)

    return dp[0][n - 1]


def solve():
    with open("task10_4.txt", "r") as f:
        while True:
            line = f.readline()
            if not line:
                break

            A = int(line.strip())
            if A == 0:
                break

            B = int(f.readline().strip())
            cuts = list(map(int, f.readline().split()))

            result = min_cut_cost(A, cuts)
            print(f"The minimum cutting price is {result}.")


if __name__ == "__main__":
    solve()
