import random

# Problem-specific data
values = [20, 90, 140]  # Values of the items
weights = [10, 25, 20]  # Weights of the items
capacity = 50  # Knapsack capacity

# Number of items
n = len(values)

# Parameters for the genetic algorithm
population_size = 10
generations = 100
mutation_rate = 0.01
crossover_rate = 0.7

# Fitness function: Total value of items in the knapsack (if the weight is within the capacity)
def fitness(solution):
    total_weight = sum(solution[i] * weights[i] for i in range(n))
    if total_weight > capacity:
        return 0  # Penalty: if weight exceeds the capacity
    total_value = sum(solution[i] * values[i] for i in range(n))
    return total_value

# Generate a random solution (individual)
def random_solution():
    return [random.randint(0, 1) for _ in range(n)]

# Tournament selection (select two parents)
def tournament_selection(population):
    selected = random.sample(population, 3)
    selected.sort(key=lambda x: fitness(x), reverse=True)
    return selected[0], selected[1]

# Crossover (single-point crossover)
def crossover(parent1, parent2):
    if random.random() > crossover_rate:
        return parent1[:], parent2[:]  # No crossover, return parents as is
    crossover_point = random.randint(1, n-1)
    child1 = parent1[:crossover_point] + parent2[crossover_point:]
    child2 = parent2[:crossover_point] + parent1[crossover_point:]
    return child1, child2

# Mutation (flip a random bit in the solution)
def mutate(solution):
    if random.random() > mutation_rate:
        return solution
    mutation_point = random.randint(0, n-1)
    solution[mutation_point] = 1 - solution[mutation_point]  # Flip bit
    return solution

# Genetic Algorithm main loop
def genetic_algorithm():
    # Initialize population with random solutions
    population = [random_solution() for _ in range(population_size)]
    
    for generation in range(generations):
        # Evaluate fitness of the population
        population.sort(key=lambda x: fitness(x), reverse=True)
        
        # If the best solution's fitness is optimal, break early
        if fitness(population[0]) == sum(values):  # Can be adjusted based on the problem
            print(f"Optimal solution found at generation {generation}")
            break
        
        # Create the next generation
        next_generation = []
        while len(next_generation) < population_size:
            # Select parents
            parent1, parent2 = tournament_selection(population)
            # Perform crossover to produce children
            child1, child2 = crossover(parent1, parent2)
            # Apply mutation
            child1 = mutate(child1)
            child2 = mutate(child2)
            # Add children to next generation
            next_generation.extend([child1, child2])
        
        # Replace the old population with the new generation
        population = next_generation[:population_size]
    
    # Return the best solution
    best_solution = population[0]
    return best_solution, fitness(best_solution)

# Run the genetic algorithm
best_solution, best_value = genetic_algorithm()

print("Best solution:", best_solution)
print("Total value:", best_value)
