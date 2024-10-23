class MapColoring:
    def __init__(self, graph, colors):
        self.graph = graph  # adjacency list of the graph
        self.colors = colors  # list of available colors
        self.assignments = {}  # store color assignments for each region

    def is_safe(self, node, color):
        # Check if the color assignment is safe
        for neighbor in self.graph[node]:
            if neighbor in self.assignments and self.assignments[neighbor] == color:
                return False
        return True

    def backtrack(self):
        # Try to color each region
        if len(self.assignments) == len(self.graph):
            return True  # All regions are colored

        for node in self.graph:
            if node not in self.assignments:
                for color in self.colors:
                    if self.is_safe(node, color):
                        self.assignments[node] = color  # Assign color
                        if self.backtrack():
                            return True
                        del self.assignments[node]  # Backtrack

                return False  # No color was safe for this node
        return False

    def solve(self):
        if self.backtrack():
            return self.assignments
        else:
            return None  # No solution found


if __name__ == "__main__":
    # Example graph as an adjacency list
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B', 'E'],
        'E': ['B', 'D'],
        'F': ['C']
    }

    colors = ['Red', 'Green', 'Blue']  # Available colors
    map_coloring = MapColoring(graph, colors)
    solution = map_coloring.solve()

    if solution:
        print("Map coloring solution:")
        for region, color in solution.items():
            print(f"Region {region} is colored {color}.")
    else:
        print("No solution found.")
