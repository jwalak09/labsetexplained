# Hill Climbing Algorithm

import random


def fitness(sol):
    """
    Fitness function to evaluate the quality of a solution.
    In this case, the fitness is simply the sum of the solution vector.
    """
    return sum(sol)


def solution(num):
    """
    Hill Climbing algorithm to find the best solution.

    Parameters:
    num (int): The length of the solution vector.

    Returns:
    best_soln (list): The best solution found.
    best_fit (int): The fitness of the best solution.
    """
    # Initialize a random solution vector of length 'num'
    current_soln = [random.randint(0, 1) for _ in range(0, num)]

    # Evaluate the fitness of the initial solution
    current_fit = fitness(current_soln)

    while True:
        # Choose a random index to start the climbing
        index = random.randint(0, num - 1)

        # Create a copy of the current solution to generate a neighbor
        neighbor = current_soln[:]

        # Flip the binary value at the chosen index to generate a new neighbor
        neighbor[index] = 1 - neighbor[index]

        # Evaluate the fitness of the neighbor solution
        neighbor_fit = fitness(neighbor)

        # If the neighbor solution is better (i.e., has higher fitness),
        # update the current solution and fitness.
        if neighbor_fit >= current_fit:
            current_fit = neighbor_fit
            current_soln = neighbor
        else:
            # If the neighbor solution is not better, break the loop
            break

    # Return the best solution and its fitness
    return current_soln, current_fit


# Specify the length of the solution vector (can be random)
num = 3

# Run the Hill Climbing algorithm
best_soln, best_fit = solution(num)

# Print the best solution and its fitness
print('Best solution:', best_soln)
print('Best fitness:', best_fit)