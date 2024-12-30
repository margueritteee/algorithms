import random
#selecting individuals from a given population based on their fitness scores
def selection(population, fitness_scores):
    tournament_size = 3 #the number of individuals randomly chosen to compete in each tournament
    selected = [] #will store the individuals chosen
    for _ in range(len(population)):
        tournament = random.sample(list(enumerate(population)), tournament_size)
        winner = max(tournament, key=lambda x: fitness_scores[x[0]])
        selected.append(winner[1])
    return selected
