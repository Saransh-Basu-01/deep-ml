def matrixmul(a:list[list[int|float]],
              b:list[list[int|float]])-> list[list[int|float]]:
    A,B=len(a),len(a[0])
    C,D=len(b),len(b[0])
    result = [[0] * D for _ in range(A)]
    if B!=C:
        return -1
    else:
        for i in range(A):
            for j in range(D):
                s=0
                for k in range(B):
                    s+=a[i][k]*b[k][j]
                result[i][j]=s
        return result
        