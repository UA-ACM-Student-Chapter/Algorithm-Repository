from constants import  inf, neginf
from collections import deque


class Vertex(object):

    def __init__(self, label=None, edges=None):
        self.label = label
        self.edges = edges or []

    def add_edge(self, edge):
        self.edges.append(edge)


class Edge(object):

    def __init__(self, from_vertex=None, to_vertex=None, weight=1):
        self.from_vertex = from_vertex
        self.to_vertex = to_vertex
        self.weight = weight
        from_vertex.add_edge(self)

    def __str__(self):
        return 'edge from ' + str(self.from_vertex.label) + ' to ' + str(self.to_vertex.label)


class Graph(object):

    def __init__(self, verticies, edges):
        self.verticies = verticies or []
        self.edges = edges or []

    def __init__(self, adjacency_matrix):

        self.verticies = []
        self.edges = []

        for i in range(0, len(adjacency_matrix)):
            self.add_vertex(Vertex(i))

        for i in range(0, len(adjacency_matrix)):
            for j in range(0, len(adjacency_matrix[i])):
                if adjacency_matrix[i][j] != inf:
                    self.add_edge(Edge(from_vertex=self.verticies[i],
                                       to_vertex=self.verticies[j], weight=adjacency_matrix[i][j]))

    def add_vertex(self, vertex):
        self.verticies.append(vertex)

    def add_edge(self, edge):
        self.edges.append(edge)

    def bfs(self):
        seen = [False for _ in range(len(self.verticies))]
        seen[0] = True
        queue = deque([(None, self.verticies[0])])
        while len(queue) > 0:
            e, vertex = queue.popleft()
            for edge in vertex.edges:
                if not seen[edge.to_vertex.label] and edge.weight > 0:
                    seen[edge.to_vertex.label] = True
                    queue.append((edge, edge.to_vertex))
            yield (e, vertex)

    def find_augmenting_path(self):
        parents = [None for _ in range(0, len(self.verticies))]

        for edge, vertex in self.bfs():
            parents[vertex.label] = edge
            if vertex.label == self.verticies[-1].label:
                path = []
                min_weight = inf
                current = parents[vertex.label]
                while current is not None:
                    min_weight = min(min_weight, current.weight)
                    path.insert(0, current)
                    current = parents[current.from_vertex.label]
                return (min_weight, path)
        return None


    def max_flow(self):
        flows = [0 for _ in range(0, len(self.edges))]





def tester():
    g = Graph(adjacency_matrix=[
        # s
        [0, 3, 10, 6, 5, inf],
        # a
        [inf, 0, 2, inf, inf, 5],
        # b
        [inf, 1, 0, 2, inf, 6],
        # c
        [inf, inf, 1, 0, 2, 10],
        # d
        [inf, inf, inf, 1, 0, 3],
        # t
        [inf, inf, inf, inf, inf, inf]
    ])

    for e, v in g.bfs():
        print v.label

    min, path =  g.find_augmenting_path()
    for edge in path:
        print edge.from_vertex.label, ',', edge.to_vertex.label

if __name__ == '__main__':
    tester()