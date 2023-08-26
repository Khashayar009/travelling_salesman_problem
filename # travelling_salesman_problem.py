# travelling_salesman_problem


import itertools

def tsp(graph, start):
    # Get all possible permutations of cities
    cities = list(graph.keys())
    perm = list(itertools.permutations(cities))

    shortest_path = None
    shortest_distance = float('inf')

    for p in perm:
        distance = 0
        current_city = start

        # Calculate the distance for current permutation
        for city in p:
            distance += graph[current_city][city]
            current_city = city

        # Add the distance from the last city to the start city
        distance += graph[current_city][start]

        # Update shortest path and shortest distance if necessary
        if distance < shortest_distance:
            shortest_distance = distance
            shortest_path = p

    return shortest_path, shortest_distance

# Example usage
graph = {
    'A': {'A': 0, 'B': 10, 'C': 15, 'D': 20},
    'B': {'A': 10, 'B': 0, 'C': 35, 'D': 25},
    'C': {'A': 15, 'B': 35, 'C': 0, 'D': 30},
    'D': {'A': 20, 'B': 25, 'C': 30, 'D': 0}
}

start_city = 'A'
shortest_path, shortest_distance = tsp(graph, start_city)

print(f"Shortest Path: {' -> '.join(shortest_path)}")
print(f"Shortest Distance: {shortest_distance}")