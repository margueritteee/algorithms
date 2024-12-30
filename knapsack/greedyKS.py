def is_valid_ks(X, W, n, W_max):
    s = sum(X[i] * W[i] for i in range(n))
    return s <= W_max

def greedy_ks(W, P, n, W_max):
    # Calcul des ratios et indices
    ratio = [(P[i] / W[i], i) for i in range(n)]
    # Tri des ratios par ordre décroissant
    ratio.sort(reverse=True, key=lambda x: x[0])

    # Initialisation de X
    X = [0] * n

    # Choix glouton
    for _, i in ratio:
        X[i] = 1
        if not is_valid_ks(X, W, n, W_max):
            X[i] = 0

    return X

def main():
    W = [4, 3, 5, 2, 1]
    P = [25, 35, 55, 15, 45]
    W_max = 7
    n = len(W)

    X = greedy_ks(W, P, n, W_max)

    total_value = sum(X[i] * P[i] for i in range(n)) #calcule total value
    
    print("Solution X:", X)
    print("Total Value:", total_value)

if __name__ == "__main__":
    main()
