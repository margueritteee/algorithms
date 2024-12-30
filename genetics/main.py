from initialize import initialize_population
from fitness import fitness_function
from selection import selection
from crossover import crossover
from mutation import mutation

def main():
    values = [60, 100, 120, 80, 90]
    weights = [10, 20, 30, 15, 25]
    max_weight = 50
    
    pop_size = 10 #(population size) is the number of individuals/solutions in each generation of the genetic algorithm
    generations = 20
    
    population = initialize_population(pop_size, len(values))
    best_solution = None
    best_fitness = 0
    
    for generation in range(generations):
        fitness_scores = [fitness_function(chrom, values, weights, max_weight) 
                         for chrom in population]
        
        current_best = max(fitness_scores)
        if current_best > best_fitness:
            best_fitness = current_best
            best_solution = population[fitness_scores.index(current_best)]
        
        selected = selection(population, fitness_scores)
        
        new_population = []
        for i in range(0, pop_size, 2):
            child1, child2 = crossover(selected[i], selected[i+1])
            new_population.extend([child1, child2])
        
        population = [mutation(chrom) for chrom in new_population]
        
        print(f"Generation {generation}: Best Value = {max(fitness_scores)}")

    
    selected_items = [i for i, gene in enumerate(best_solution) if gene == 1]
    total_weight = sum(weights[i] for i in selected_items)
    
    print("\nFinal Solution:")
    print(f"Selected items (index): {selected_items}")
    print("Selected items details:")
    for item in selected_items:
        print(f"Item {item}: Value = {values[item]}, Weight = {weights[item]}")
    print(f"Total value: {best_fitness}")
    print(f"Total weight: {total_weight}/{max_weight}")

if __name__ == "__main__":
    main()
