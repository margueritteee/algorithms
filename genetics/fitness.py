def fitness(chromosome, weights, profits, capacity): #fun that calculate total weight and profit for a solution 
    #chromosone:list of 0,1 (0 not included 1 it is )
    #weights: list of weights d'objets , profits : list of profits d'objets , capacity:total weight de sac a dos
    weight = sum(w * g for w, g in zip(weights, chromosome)) #calculate total weight of objects selected by chromosome 
    #zip function in python it pairs each element with the other kima hna each weight with chromosome (selected wla wlo) w*g : ndrbo kol weight ema gen 
    if weight > capacity:
        return 0 #nverifier ida akbr tkhrj error 
    return sum(p * g for p, g in zip(profits, chromosome)) #ida msh akbr nhsbo el profitis mtali

