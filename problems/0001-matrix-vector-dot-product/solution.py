def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
    # Return a list where each element is the dot product of a row of 'a' with 'b'.
    # If the number of columns in 'a' does not match the length of 'b', return -1.
    
    # Check if the number of columns in matrix 'a' matches the length of vector 'b'
    if not a:  # Empty matrix
        return -1
    
    cols_in_a = len(a[0])
    if cols_in_a != len(b):
        return -1
    
    result = []
    
    # For each row in matrix 'a'
    for row in a:
        # Check if all rows have the same number of columns
        if len(row) != cols_in_a:
            return -1
        
        # Compute dot product of row with vector 'b'
        dot_product = 0
        for i in range(len(b)):
            dot_product += row[i] * b[i]
        
        result.append(dot_product)
    
    return result