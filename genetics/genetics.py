import random

#Generate Random Population
def generate_population(pop_size, chromosome_length):
    population = []
    for _ in range(pop_size):
        chromosome = [random.randint(0, 1) for _ in range(chromosome_length)]
        population.append(chromosome)
    return population

#Evaluation (for knapsack problem)
def evaluate(chromosome, values, weights, capacity):
    total_value = 0
    total_weight = 0
    for i in range(len(chromosome)):
        if chromosome[i] == 1:
            total_value += values[i]
            total_weight += weights[i]
    # Return 0 if weight exceeds capacity
    return 0 if total_weight > capacity else total_value

#Selection (tournament selection)
def selection(population, fitness_scores, tournament_size=2):
    tournament = random.sample(list(enumerate(fitness_scores)), tournament_size)
    winner = max(tournament, key=lambda x: x[1])[0]
    return population[winner]

#Crossover (single-point)
def crossover(parent1, parent2):
    point = random.randint(1, len(parent1)-1)
    child1 = parent1[:point] + parent2[point:]
    child2 = parent2[:point] + parent1[point:]
    return child1, child2

#Mutation
def mutation(chromosome, mutation_rate=0.1):
    mutated = chromosome.copy()
    for i in range(len(mutated)):
        if random.random() < mutation_rate:
            mutated[i] = 1 - mutated[i]  # Flip bit
    return mutated

# Example usage:
if __name__ == "__main__":
    # Example parameters
    pop_size = 4
    chromosome_length = 5
    values = [10, 20, 30, 40, 50]
    weights = [5, 10, 15, 20, 25]
    capacity = 30

    # Generate initial population
    population = generate_population(pop_size, chromosome_length)
    print("Initial population:", population)

    # Evaluate population
    fitness_scores = [evaluate(chrom, values, weights, capacity) for chrom in population]
    print("Fitness scores:", fitness_scores)

    # Selection example
    selected = selection(population, fitness_scores)
    print("Selected chromosome:", selected)

    # Crossover example
    parent1 = population[0]
    parent2 = population[1]
    child1, child2 = crossover(parent1, parent2)
    print("Children after crossover:", child1, child2)

    # Mutation example
    mutated = mutation(child1)
    print("Chromosome after mutation:", mutated)