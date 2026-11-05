def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
    if not matrix or not matrix[0]:
        return []

    m, n = len(matrix), len(matrix[0])

    if mode == "row":
        return [sum(row) / n for row in matrix]

    if mode == "column":
        return [sum(matrix[i][j] for i in range(m)) / m for j in range(n)]

    raise ValueError(f"Invalid mode: {mode!r} (expected 'row' or 'column')")