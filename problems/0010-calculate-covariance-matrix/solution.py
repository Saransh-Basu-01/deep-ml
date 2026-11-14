def calculate_covariance_matrix(vectors: list[list[float]]) -> list[list[float]]:
    # Your code here
    m=len(vectors)
    n=len(vectors[0])
    means_centered=[]
    for vector in vectors:
        mean=sum(vector)/len(vector)
        v=[i-mean for i in vector]
        means_centered.append(v)
    # result=[[0]*m for _ in range(m)]
    # for i in range(m):
    #     for j in range(m):
    #         s=0
    #         for k in range(n):
    #             s+=means_centered[i][k]* means_centered[j][k]
    #         result[i][j]=s/(n-1)
    # return result
    def dot(u, w):
        return sum(a * b for a, b in zip(u, w))

    # 3. build m x m matrix
    return [[dot(means_centered[i], means_centered[j]) / (n - 1)
             for j in range(m)]
            for i in range(m)]
