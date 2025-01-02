import random
# function modifies a chromosome by flipping some of its genes based on the mutation rate (mutation_rate: The probability of mutating each gene in the chromosome) 
def mutate(chrom, mutation_rate):
    # Generates a random number between 0 and 1 and checks if it is less than the mutation rate 1 - gene: Flips the gene:
    #If the gene is 1, it becomes 0
    #If the gene is 0, it becomes 1 
    return [1 - g if random.random() < mutation_rate else g for g in chrom]#else maysra walo haja mattbdl 
 
