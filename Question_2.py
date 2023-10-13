
class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)

    def dfs(self, vertex, visited):
        visited.add(vertex)
        print(vertex, end=" ")

        for i in self.graph.get(vertex, []):
            if i not in visited:
                self.dfs(i, visited)

graph = Graph()

while True:
    u = input("Enter a source vertex (or type 'done' to finish): ")
    if u == 'done':
        break
    v = input("Enter a destination vertex: ")
    graph.add_edge(u, v)

start = input("Enter the starting vertex for DFT: ")

print("Depth-First Traversal:")
visited = set()
graph.dfs(start, visited)
