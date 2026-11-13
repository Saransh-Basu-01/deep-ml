import numpy as np

def transform_matrix(A: list[list[int|float]], T: list[list[int|float]], S: list[list[int|float]]) -> list[list[int|float]]:
    A=np.asarray(A)
    T=np.asarray(T)
    S=np.asarray(S)
    if np.linalg.det(T)!=0 and np.linalg.det(S)!=0:
        m=A @ S
        result=np.linalg.inv(T) @ m
        return result
    else:
        return -1
        