import numpy as np

def initialize_population(pop_size, num_items):
    return [np.random.randint(2, size=num_items) for _ in range(pop_size)]