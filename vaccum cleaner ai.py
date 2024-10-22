import random

# Environment class
class Environment:
    def __init__(self, size=(2, 2)):
        self.size = size
        # Create a grid where 1 represents dirty and 0 represents clean
        self.grid = [[random.choice([0, 1]) for _ in range(size[1])] for _ in range(size[0])]

    def is_dirty(self, x, y):
        return self.grid[x][y] == 1

    def clean(self, x, y):
        self.grid[x][y] = 0

    def display(self):
        for row in self.grid:
            print(row)
        print()


# Vacuum Cleaner Agent
class VacuumCleanerAgent:
    def __init__(self, environment):
        self.environment = environment
        self.x = 0
        self.y = 0

    def move(self, direction):
        if direction == 'up' and self.x > 0:
            self.x -= 1
        elif direction == 'down' and self.x < self.environment.size[0] - 1:
            self.x += 1
        elif direction == 'left' and self.y > 0:
            self.y -= 1
        elif direction == 'right' and self.y < self.environment.size[1] - 1:
            self.y += 1

    def clean(self):
        if self.environment.is_dirty(self.x, self.y):
            print(f"Cleaning room at ({self.x}, {self.y})")
            self.environment.clean(self.x, self.y)

    def act(self):
        directions = ['up', 'down', 'left', 'right']
        while any(1 in row for row in self.environment.grid):  # Keep cleaning until all rooms are clean
            self.clean()
            # Move in a random direction
            direction = random.choice(directions)
            self.move(direction)
            print(f"Moved {direction} to ({self.x}, {self.y})")
            self.environment.display()

# Create the environment and the agent
env = Environment(size=(2, 2))
vacuum_agent = VacuumCleanerAgent(env)

# Display the initial state of the environment
print("Initial Environment:")
env.display()

# Agent starts acting
vacuum_agent.act()

# Final state of the environment
print("Final Environment:")
env.display()
