def spiralMatrix(matrix):

    if len(matrix) == 0 or len(matrix[0]) == 0:  # len(matrix) >- number or row and len(matrix[0]) >- number of column
        return []

    m = len(matrix)
    n = len(matrix[0])
    T = 0       # top
    B = m - 1   # bottom
    L = 0       # left
    R = n - 1   # right

    direc = 0
    result = []

    while T <= B and L <= R:
        # traverse from left to right
        if direc == 0:
            for k in range(L, R + 1):
                result.append(matrix[T][k])
            T += 1
            direc = 1

        # traverse from top to bottom
        elif direc == 1:
            for k in range(T, B + 1):
                result.append(matrix[k][R])
            R -= 1
            direc = 2

        # traverse from right to left
        elif direc == 2:
            for k in range(R, L - 1, - 1):
                result.append(matrix[B][k])
            B -= 1
            direc = 3

        # traverse from bottom to up
        elif direc == 3:
            for k in range(B, T - 1, -1):
                result.append(matrix[k][L])
            L += 1
            direc = 0

    return result


num = int(input())
array = []
for _ in range(num):
    array.append(list(map(int, input().split())))

print(spiralMatrix(array))

