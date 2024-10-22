from collections import deque

# Function to check if a state has been visited before
def is_visited(state, visited):
    return state in visited

# Function to print the solution path
def print_solution(path):
    for step in path:
        print(f"Jug X: {step[0]} liters, Jug Y: {step[1]} liters")

# Function to solve the water jug problem using BFS
def water_jug_bfs(capacity_x, capacity_y, target):
    # Queue for BFS
    queue = deque([(0, 0)])  # Initial state: both jugs empty
    visited = set([(0, 0)])  # To keep track of visited states
    parent = {}  # To store the path

    while queue:
        x, y = queue.popleft()

        # If the target is achieved, print the solution path
        if x == target or y == target:
            path = []
            while (x, y) in parent:
                path.append((x, y))
                x, y = parent[(x, y)]
            path.append((x, y))
            path.reverse()
            print_solution(path)
            return

        # Generate all possible next states
        possible_states = [
            (capacity_x, y),  # Fill Jug X
            (x, capacity_y),  # Fill Jug Y
            (0, y),           # Empty Jug X
            (x, 0),           # Empty Jug Y
            (min(x + y, capacity_x), y - (min(x + y, capacity_x) - x)) if y > 0 else (x, y),  # Pour Jug Y -> X
            (x - (min(x + y, capacity_y) - y), min(x + y, capacity_y)) if x > 0 else (x, y),  # Pour Jug X -> Y
        ]

        # Explore each state
        for new_state in possible_states:
            if not is_visited(new_state, visited):
                queue.append(new_state)
                visited.add(new_state)
                parent[new_state] = (x, y)

    print("No solution found.")

# Example usage:
capacity_x = 4  # Capacity of Jug X
capacity_y = 3  # Capacity of Jug Y
target = 2      # Target amount of water

water_jug_bfs(capacity_x, capacity_y, target)
