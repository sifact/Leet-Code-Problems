def transpose(A):
    m = len(A)
    n = len(A[0])

    matrix = []

    for j in range(n):
        tmp = []
        for i in range(m):
            tmp.append(A[i][j])
        matrix.append(tmp)

    return matrix


m1 = []
for _ in range(int(input())):
    m1.append(list(map(int, input().split())))

print(transpose(m1))
