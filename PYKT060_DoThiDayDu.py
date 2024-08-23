def read_input():
    n, m = int(input()), int(input())
    edges = [list(map(int, input().split())) for _ in range(m)]
    return n, m, edges


def build_graph(n, edges):
    graph = [[0] * (n + 1) for _ in range(n + 1)]
    for x, y in edges:
        graph[x][y] = graph[y][x] = 1
    return graph


def find_connected_components(n, edges):
    parent = [-1] * (n + 1)
    rank = [0] * (n + 1)

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        xroot, yroot = find(x), find(y)
        if xroot == yroot:
            return
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    for i in range(1, n + 1):
        parent[i] = i

    for x, y in edges:
        union(x, y)

    components = {}
    for i in range(1, n + 1):
        root = find(i)
        if root not in components:
            components[root] = set()
        components[root].add(i)

    return list(components.values())


def is_complete(graph, component):
    for x in component:
        for y in component:
            if x != y and graph[x][y] == 0:
                return False
    return True


def main():
    n, m, edges = read_input()
    graph = build_graph(n, edges)
    components = find_connected_components(n, edges)

    if all(is_complete(graph, component) for component in components):
        print('YES')
    else:
        print('NO')


if __name__ == "__main__":
    main()