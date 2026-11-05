import numpy as np

def reshape_matrix(a: list[list[int | float]], new_shape: tuple[int, int]) -> list[list[int | float]]:
    a_t = np.asarray(a)
    if a_t.size != new_shape[0] * new_shape[1]:
        return []
    reshaped_matrix = np.reshape(a_t, new_shape)
    return reshaped_matrix.tolist()