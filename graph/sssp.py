
inf = float('inf')

def init_single_source(n, s):
    distances = [ inf for x in range(0, n)]
    parents = [ None for x in range(0, n)]
    distances[s] = 0
    return (distances, parents)

def relax(u, v, distances, parents, w):
    if distances[v] > distances[u] + w[u][v]:
        distances[v] = distances[u] + w[u][v]
        parents[v] = u

def bellman_ford(w, s):
    n = len(w)
    distances, parents = init_single_source(n, s)
    for i in range(0, n - 1):
        for u in range(0, n):
            for v in range(0, n):
                if w[u][v] != inf:
                    relax(u, v, distances, parents, w)
    for u in range(0, n):
        for v in range(0, n):
            if w[u][v] != inf:
                if distances[v] > distances[u] + w[u][v]:
                    return False # negative weight cycle
    return (distances, parents)

graph = [
    [0, 0, 0, 0, 0, 0, 0],
    [inf, 0, inf, inf, inf, -1, inf],
    [inf, 1, 0, inf, 2, inf, inf],
    [inf, inf, 2, 0, inf, inf, -8],
    [inf, -4, inf, inf, 0, 3, inf],
    [inf, inf, 7, inf, inf, 0, inf],
    [inf, inf, 5, 10, inf, inf, 0]
]

print bellman_ford(graph, 0)

    
