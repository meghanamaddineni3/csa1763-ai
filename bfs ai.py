from collections import deque

# Function to perform BFS
def bfs(graph, start):
    visited = set()  # A set to keep track of visited nodes
    queue = deque([start])  # Initialize a queue with the starting node

    while queue:
        # Dequeue a vertex from the queue
        vertex = queue.popleft()

        # If this node hasn't been visited yet
        if vertex not in visited:
            print(vertex, end=" ")  # Process the node (print it)
            visited.add(vertex)  # Mark the node as visited

            # Add all unvisited neighbors of the current node to the queue
            for neighbor in graph[vertex]:
                if neighbor not in visited:
                    queue.append(neighbor)

# Example usage
if __name__ == "__main__":
    # A sample graph represented as an adjacency list
    graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': [],
        'E': ['F'],
        'F': []
    }

    print("BFS Traversal starting from node A:")
    bfs(graph, 'A')
