def knapsack_brute_force(values, weights, capacity):
    """
    Solve the 0/1 knapsack problem using brute force approach.
    
    Args:
        values (list): List of values for each item
        weights (list): List of weights for each item
        capacity (int): Maximum weight capacity of knapsack
    
    Returns:
        tuple: (maximum value possible, list of selected items)
    """
    n = len(values)
    max_value = 0
    best_selection = []
    
    # Try all possible combinations (2^n)
    for i in range(2 ** n):
        current_value = 0
        current_weight = 0
        current_selection = []
        
        # Check each bit position
        for j in range(n):
            # If jth bit is set in i
            if i & (1 << j):
                current_value += values[j]
                current_weight += weights[j]
                current_selection.append(j)
        
        # Update max_value if this combination is valid and better
        if current_weight <= capacity and current_value > max_value:
            max_value = current_value
            best_selection = current_selection.copy()
    
    return max_value, best_selection

# Example usage
if __name__ == "__main__":
    # Example problem
    values = [80, 120, 90]
    weights = [15, 25, 20]
    capacity = 50
    
    max_value, selected_items = knapsack_brute_force(values, weights, capacity)
    
    print(f"Maximum value possible: {max_value}")
    print("Selected items (indices):", selected_items)
    print("\nDetailed selection:")
    for idx in selected_items:
        print(f"Item {idx}: Value = {values[idx]}, Weight = {weights[idx]}")