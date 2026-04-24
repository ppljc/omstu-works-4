from collections import deque


class MaxFlow:
    def __init__(self, n):
        self.n = n
        self.graph = [[] for _ in range(n)]
        self.capacity = {}

    def add_edge(self, u, v, cap):
        self.graph[u].append(v)
        self.graph[v].append(u)
        self.capacity[(u, v)] = cap
        self.capacity[(v, u)] = 0

    def bfs(self, s, t, parent):
        visited = [False] * self.n
        queue = deque([s])
        visited[s] = True
        while queue:
            u = queue.popleft()
            for v in self.graph[u]:
                if not visited[v] and self.capacity.get((u, v), 0) > 0:
                    parent[v] = u
                    visited[v] = True
                    if v == t:
                        return True
                    queue.append(v)
        return False

    def edmonds_karp(self, s, t):
        parent = [-1] * self.n
        max_flow = 0
        while self.bfs(s, t, parent):
            path_flow = float('Inf')
            s_curr = t
            while s_curr != s:
                path_flow = min(path_flow, self.capacity[(parent[s_curr], s_curr)])
                s_curr = parent[s_curr]
            max_flow += path_flow
            v = t
            while v != s:
                u = parent[v]
                self.capacity[(u, v)] -= path_flow
                self.capacity[(v, u)] += path_flow
                v = parent[v]
        return max_flow


def solve_task_setter(nk, np, categories_needed, task_to_cats):
    source = 0
    sink = np + nk + 1
    flow_net = MaxFlow(sink + 1)

    total_needed = sum(categories_needed)

    for i in range(1, np + 1):
        flow_net.add_edge(source, i, 1)

    for task_idx, cats in enumerate(task_to_cats, 1):
        for cat in cats:
            flow_net.add_edge(task_idx, np + cat, 1)

    for cat_idx, needed in enumerate(categories_needed, 1):
        flow_net.add_edge(np + cat_idx, sink, needed)

    max_flow = flow_net.edmonds_karp(source, sink)

    if max_flow == total_needed:
        result = [[] for _ in range(nk)]
        for task_idx in range(1, np + 1):
            for v in flow_net.graph[task_idx]:
                if np < v <= np + nk and flow_net.capacity[(task_idx, v)] == 0:
                    cat_idx = v - np - 1
                    result[cat_idx].append(task_idx)
        return 1, result
    else:
        return 0, None


def main():
    try:
        input_data = open('task10_4.txt', 'r').read().split()
    except FileNotFoundError:
        return

    it = iter(input_data)

    while True:
        try:
            nk = int(next(it))
            np = int(next(it))
        except StopIteration:
            break

        if nk == 0 and np == 0:
            break

        categories_needed = [int(next(it)) for _ in range(nk)]
        task_to_cats = []
        for _ in range(np):
            num_cats = int(next(it))
            task_to_cats.append([int(next(it)) for _ in range(num_cats)])

        status, result = solve_task_setter(nk, np, categories_needed, task_to_cats)

        print(status)
        if status == 1:
            for row in result:
                print(*row)


if __name__ == "__main__":
    main()
