class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)

    def cycle(self):
        visited = set()
        rec_stack = set()

        def dfs(node):
            visited.add(node)
            rec_stack.add(node)

            for i in self.graph.get(node, []):
                if i not in visited:
                    if dfs(i):
                        return True
                elif i in rec_stack:
                    return True

            rec_stack.remove(node)
            return False

        for node in self.graph:
            if node not in visited:
                if dfs(node):
                    return True

        return False


graph = Graph()

while True:
    u = input("Enter a source vertex (or type 'done' to finish): ")
    if u == 'done':
        break
    v = input("Enter a destination vertex: ")
    graph.add_edge(u, v)

if graph.cycle():
    print("\nThe directed graph contains a cycle.")
else:
    print("\nThe directed graph does not contain a cycle.")
