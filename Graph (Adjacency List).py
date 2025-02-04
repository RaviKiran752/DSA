class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)

    def print_graph(self):
        for node in self.graph:
            print(node, "->", self.graph[node])

# Usage
g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.print_graph()  
# Output:
# 0 -> [1, 2]
