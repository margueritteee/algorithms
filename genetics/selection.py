import random

def selection(population, fitness_scores):
    tournament_size = 3
    selected = []
    for _ in range(len(population)):
        tournament = random.sample(list(enumerate(population)), tournament_size)
        winner = max(tournament, key=lambda x: fitness_scores[x[0]])
        selected.append(winner[1])
    return selected