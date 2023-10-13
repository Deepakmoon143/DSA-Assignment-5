class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append(v)
        self.graph[v].append(u)

    def dfs(self, vertex, visited):
        visited.add(vertex)
        for i in self.graph.get(vertex, []):
            if i not in visited:
                self.dfs(i, visited)

def count_trees_in_forest(graph):
    visited = set()
    tree_count = 0

    for i in graph.graph:
        if i not in visited:
            graph.dfs(i, visited)
            tree_count += 1

    return tree_count

forest = Graph()

while True:
    u = input("Enter a source vertex (or type 'done' to finish): ")
    if u == 'done':
        break

    v = input("Enter a destination vertex: ")
    forest.add_edge(u, v)

tree = count_trees_in_forest(forest)

print(f"Number of trees in the forest: {tree}")
