# Python program to implement DFS in a graph

# Graph represented as an adjacency list
class Graph:
    def __init__(self):
        self.graph = {}

    # Add edge to the graph
    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)

    # DFS function
    def dfs(self, start_vertex, visited=None):
        if visited is None:
            visited = set()  # Track visited nodes

        # Mark the current node as visited
        visited.add(start_vertex)
        print(start_vertex, end=" ")

        # Recur for all the vertices adjacent to the current vertex
        for neighbor in self.graph.get(start_vertex, []):
            if neighbor not in visited:
                self.dfs(neighbor, visited)


# Example usage
g = Graph()

# Add edges to the graph (example graph)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)

print("Depth-First Search starting from vertex 2:")
g.dfs(2)
