import math

def calculate_eigenvalues(matrix: list[list[float | int]]) -> list[float]:
    # Validate shape
    if len(matrix) != 2 or any(len(row) != 2 for row in matrix):
        raise ValueError("Expected a 2x2 matrix")

    a, b = matrix[0]
    c, d = matrix[1]

    trace = a + d
    det = a * d - b * c
    disc = trace * trace - 4 * det

    if disc < 0:
        raise ValueError("Complex eigenvalues not supported by return type")

    sqrt_disc = math.sqrt(disc)
    return [(trace + sqrt_disc) / 2, (trace - sqrt_disc) / 2]