def fitness_function(chromosome, values, weights, max_weight):
    total_value = sum(v for i, v in enumerate(values) if chromosome[i])
    total_weight = sum(w for i, w in enumerate(weights) if chromosome[i])
    return 0 if total_weight > max_weight else total_value