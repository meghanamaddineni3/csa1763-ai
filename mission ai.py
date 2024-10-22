from collections import deque

# Function to check if the current state is valid
def is_valid_state(missionaries, cannibals):
    if missionaries < 0 or cannibals < 0 or missionaries > 3 or cannibals > 3:
        return False
    if missionaries > 0 and missionaries < cannibals:  # Missionaries eaten
        return False
    return True

# Function to check if the current state is the goal state
def is_goal_state(state):
    return state == (0, 0, 1)

# Function to generate all possible next states
def get_next_states(state):
    missionaries_left, cannibals_left, boat = state
    if boat == 1:  # Boat is on the starting side
        possible_moves = [(1, 0), (2, 0), (0, 1), (1, 1), (0, 2)]  # Possible moves: (missionaries, cannibals)
        for move in possible_moves:
            new_missionaries_left = missionaries_left - move[0]
            new_cannibals_left = cannibals_left - move[1]
            new_missionaries_right = 3 - new_missionaries_left
            new_cannibals_right = 3 - new_cannibals_left
            new_state = (new_missionaries_left, new_cannibals_left, 0)  # Boat goes to the other side
            if is_valid_state(new_missionaries_left, new_cannibals_left) and is_valid_state(new_missionaries_right, new_cannibals_right):
                yield new_state
    else:  # Boat is on the opposite side
        possible_moves = [(1, 0), (2, 0), (0, 1), (1, 1), (0, 2)]
        for move in possible_moves:
            new_missionaries_left = missionaries_left + move[0]
            new_cannibals_left = cannibals_left + move[1]
            new_missionaries_right = 3 - new_missionaries_left
            new_cannibals_right = 3 - new_cannibals_left
            new_state = (new_missionaries_left, new_cannibals_left, 1)  # Boat goes back to the start side
            if is_valid_state(new_missionaries_left, new_cannibals_left) and is_valid_state(new_missionaries_right, new_cannibals_right):
                yield new_state

# Function to solve the Missionaries and Cannibals problem using BFS
def solve_missionaries_cannibals():
    initial_state = (3, 3, 1)  # (Missionaries, Cannibals, Boat on starting side)
    goal_state = (0, 0, 0)
    
    # Queue for BFS
    queue = deque([(initial_state, [])])
    visited = set([initial_state])

    while queue:
        current_state, path = queue.popleft()

        # If goal is reached, return the solution path
        if current_state == goal_state:
            return path + [current_state]

        # Generate next states and explore them
        for next_state in get_next_states(current_state):
            if next_state not in visited:
                visited.add(next_state)
                queue.append((next_state, path + [current_state]))

    return None  # No solution found

# Function to print the solution path
def print_solution(solution):
    if solution:
        for i, step in enumerate(solution):
            missionaries_left, cannibals_left, boat = step
            side = "left" if boat == 1 else "right"
            print(f"Step {i}: Missionaries on left: {missionaries_left}, Cannibals on left: {cannibals_left}, Boat on {side}")
    else:
        print("No solution found.")

# Solve the problem and print the solution
solution = solve_missionaries_cannibals()
print_solution(solution)
s
