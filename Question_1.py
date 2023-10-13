class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append(v)

    def bft(self, start):
        visited = set()
        queue = []

        queue.append(start)
        visited.add(start)

        while queue:
            vertex = queue.pop(0)
            print(vertex, end=" ")

            for i in self.graph.get(vertex, []):
                if i not in visited:
                    queue.append(i)
                    visited.add(i)


graph = Graph()

while True:
    u = input("Enter a source vertex (or type 'done' to finish): ")
    if u == 'done':
        break
    v = input("Enter a destination vertex: ")
    graph.add_edge(u, v)

start = input("Enter the starting vertex for BFT: ")

print("Breadth-First Traversal:")
graph.bft(start)
