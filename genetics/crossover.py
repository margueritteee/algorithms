import random
#combining genetic information from two parent chromosomes 
def crossover(p1, p2):
    #point:index how the genetic material is splited
    point = random.randint(1, len(p1) - 1) #make sure the crossover maysrash mlwl wla tali
    return (p1[:point] + p2[point:],  #p1[:point] tdi part lwla htan l win 9smna fel parent lwl p2[point: tdi mn win point ntae t9a63 htan tali fel parent zawj 
            p2[:point] + p1[point:])
#example : (p1): [1, 0, 1, 1, 0, 1] / (p2): [0, 1, 0, 0, 1, 0] index=3 (crossover point) 
#p1(baed el t9sim):Left segment: [1, 0, 1] Right segment: [1, 0, 1] 
#p2 (baed el t9sim): Left segment: [0, 1, 0] Right segment: [0, 1, 0]
#combine left ntae p1 ema right ntae p2 : Child 1: [1, 0, 1] + [0, 1, 0] = [1, 0, 1, 0, 1, 0]
#combine left ntae p2 ema right ntae p1 : Child 2: [0, 1, 0] + [1, 0, 1] = [0, 1, 0, 1, 0, 1] 
