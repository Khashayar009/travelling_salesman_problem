# travelling_salesman_problem
This repository contains a Python implementation of the Travelling Salesman Problem (TSP) algorithm.

Description
The Travelling Salesman Problem is a classic optimization problem in computer science where the goal is to find the shortest possible route that visits all given cities and returns to the starting city. In this implementation, the TSP algorithm calculates the shortest path and distance for a given graph of cities.

Installation
To use this code, please follow these steps:

Clone the repository to your local machine using git clone <repository-url>
Navigate to the project directory
Open the travelling_salesman_problem.py file
Usage
To use the TSP algorithm, modify the graph dictionary variable to represent your own graph of cities. Each city should be represented by a unique key, and its distances to other cities should be defined as values in a nested dictionary.

Here's an example usage:

python
Copy code
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
