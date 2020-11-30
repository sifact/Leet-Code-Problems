def generateMatrix(n):
    # Declaration
    matrix = [
        [0] * n for i in range(n)
    ]

    # Edge Case
    if n == 0:
        return matrix

    # Normal Case
    T = 0
    B = n - 1
    L = 0
    R = n - 1
    num = 0

    while T <= B and L <= R:

        # traverse form left to right
        for i in range(L, R + 1):
            num += 1
            matrix[T][i] = num
        T += 1

        # traverse from top to bottom
        for i in range(T, B + 1):
            num += 1
            matrix[i][R] = num
        R -= 1

        # traverse from right to left
        for i in range(R, L - 1, -1):
            num += 1
            matrix[B][i] = num
        B -= 1

        # traverse from bottom to top
        for i in range(B, T - 1, -1):
            num += 1
            matrix[i][L] = num
        L += 1
    return matrix


nums = int(input())
print(generateMatrix(nums))
