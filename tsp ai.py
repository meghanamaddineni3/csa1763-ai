import itertools

# Define the Traveling Salesman Problem class
class TravelingSalesmanProblem:
    def __init__(self, distance_matrix):
        self.distance_matrix = distance_matrix
        self.num_cities = len(distance_matrix)

    # Calculate the total distance of a given path
    def calculate_path_distance(self, path):
        total_distance = 0
        for i in range(len(path) - 1):
            total_distance += self.distance_matrix[path[i]][path[i + 1]]
        # Return to the starting city
        total_distance += self.distance_matrix[path[-1]][path[0]]
        return total_distance

    # Brute-force approach to find the minimum distance
    def find_shortest_path(self):
        cities = list(range(self.num_cities))
        min_path = None
        min_distance = float('inf')

        # Generate all permutations of cities
        for perm in itertools.permutations(cities):
            current_distance = self.calculate_path_distance(perm)
            if current_distance < min_distance:
                min_distance = current_distance
                min_path = perm

        return min_path, min_distance

# Example usage
if __name__ == "__main__":
    # Distance matrix representing distances between cities
    distance_matrix = [
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0]
    ]

    tsp = TravelingSalesmanProblem(distance_matrix)
    shortest_path, min_distance = tsp.find_shortest_path()

    print(f"The shortest path is: {shortest_path}")
    print(f"The minimum distance is: {min_distance}")
