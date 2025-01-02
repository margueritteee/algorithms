import random
from initialize import init_population
from fitness import fitness
from selection import selection
from crossover import crossover
from mutation import mutate
#infos
weights = [10, 20, 30, 40, 50]
profits = [60, 100, 120, 240, 300]
capacity = 100
#les params
pop_size = 20
generations = 20
mutation_rate = 0.1 

def main():
    population = init_population(weights, pop_size)
    
    for gen in range(generations):
        new_pop = []
        while len(new_pop) < pop_size:
            p1, p2 = selection(population, weights, profits, capacity)
            c1, c2 = crossover(p1, p2)
            new_pop.extend([mutate(c1, mutation_rate), mutate(c2, mutation_rate)])
        
        population = new_pop[:pop_size]
        best = max(fitness(c, weights, profits, capacity) for c in population)
        print(f"Generation {gen+1}: Best Fitness = {best}")
    
    scores = [fitness(c, weights, profits, capacity) for c in population]
    best_solution = population[scores.index(max(scores))]
    return best_solution, max(scores)

if __name__ == "__main__":
    solution, profit = main()
    print("best Solution:", solution)
    print("max Profit:", profit)
