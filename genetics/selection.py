import random
from fitness import fitness

def selection(population, weights, profits, capacity):
    scores = [fitness(chrom, weights, profits, capacity) for chrom in population] #scores is a list fiha fitness values ntae kol chromosome
    total = sum(scores) #total fitness ntae population
    if total == 0:
        return random.sample(population, 2) #ida kano gae fitness ntaehm zero nkhyro 2 chromo randomly
    probs = [s / total for s in scores] #nhsbo probab ntae kol chromo ( fitness ntae kol chromo ela total fitness)
    return random.choices(population, weights=probs, k=2) #function selects parents with higher fitness scores more likely to be chosen
