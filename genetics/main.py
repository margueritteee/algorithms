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
generations = 50
mutation_rate = 0.1 

def main():
    population = init_population(weights, pop_size)
    best_ever_solution = None
    best_ever_fitness = 0
    
    for gen in range(generations):
        new_pop = []
        while len(new_pop) < pop_size:
            p1, p2 = selection(population, weights, profits, capacity)
            c1, c2 = crossover(p1, p2)
            new_pop.extend([mutate(c1, mutation_rate), mutate(c2, mutation_rate)])
        
        population = new_pop[:pop_size]
        
        # Update best solution if we find a better one
        current_best_fitness = max(fitness(c, weights, profits, capacity) for c in population)
        current_best = population[max(range(len(population)), 
                                   key=lambda i: fitness(population[i], weights, profits, capacity))]
        
        if current_best_fitness > best_ever_fitness:
            best_ever_fitness = current_best_fitness
            best_ever_solution = current_best
            
        print(f"Generation {gen+1}: Best Fitness = {current_best_fitness} (Best Ever: {best_ever_fitness})")
    
    return best_ever_solution, best_ever_fitness

if __name__ == "__main__":
    solution, profit = main()
    print("Best Solution:", solution)
    print("Max Profit:", profit)
