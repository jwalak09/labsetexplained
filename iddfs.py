from collections import deque
def iddfs(start, goal, graph):
    """
    Iterative Deepening Depth-First Search (IDDFS) algorithm.

    This function iterates through a range of depths from 1 to the number of nodes in the graph.
    It calls the dls function repeatedly with increasing depth until it finds the goal node.
    """
    depth = 0
    while True:
        # Call the dls function with the current depth
        result = dls(start, goal, graph, depth)
        if result:
            # If the goal node is found, return the path
            return result
        depth += 1


def dls(start, goal, graph, depth):
    """
    Depth-Limited Search (DLS) function.

    This function performs a depth-first search up to a given depth.
    It uses a stack to keep track of nodes to visit.
    """
    stack = deque([(start, [start], 0)])  # Initialize the stack with the starting node

    while stack:
        node, path, current_depth = stack.pop()  # Retrieve the next node to visit from the stack

        if node == goal:  # If the goal node is found, return the path
            return path

        if current_depth < depth:  # If the current depth is less than the given depth
            # Iterate over the neighbors of the current node in the graph
            for neighbor in graph[node]:
                if neighbor not in path:  # If the neighbor is not in the path, add it to the stack
                    stack.append((neighbor, path + [neighbor], current_depth + 1))

    # If the goal node is not found, return an empty tuple
    return ()


# Example graph
graph = {
    'A': ['B', 'D'],
    'B': ['A', 'C', 'G', 'E'],
    'C': ['B', 'F'],
    'D': ['A', 'E', 'G'],
    'E': ['F', 'B'],
    'F': ['E', 'C', 'G'],
    'G': ['F', 'B', 'D']
}

start = 'A'
goal = 'G'

res = iddfs(start, goal, graph)

if res is not None:
    print('Path found:', '->'.join(res))
else:
    print('Not found')