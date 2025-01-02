import random

def init_population(weights, pop_size): #function takes 2 params (weights:list of item weights / pop_size:how many solutions to create)
    return [[random.randint(0, 1) for _ in range(len(weights))] for _ in range(pop_size)] #loop for pop_size (create gdash mn solutions) / loop deuxieme len(weights)times (create one solution) w ha tkon random bin 0,1

#example :For weights=[10,20,30] and pop_size=5 [
    #[1, 0, 1],  
    #[0, 1, 0],
    #[1, 1, 0], 
    #[0, 0, 1],  
    #[1, 0, 0]] lazm tfotsh 60 we verfying the total weight in fitness fun
