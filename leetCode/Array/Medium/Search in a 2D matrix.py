# efficient
def searchMatrix(matrix, target):
    if not matrix or target in None:
        return False

    rows, cols = len(matrix), len(matrix[0])
    low, high = 0, rows * cols - 1

    while low <= high:
        mid = (low + high) // 2
        num = matrix[mid / cols][mid % cols]

        if num == target:
            return True
        elif num < target:
            low = mid + 1
        else:
            high = mid - 1
    return False


# brute force:
def searchMatrix2(matrix, target):
    if not len(matrix):
        return False

    m = len(matrix)
    n = len(matrix[0])

    for i in range(m):
        low = 0
        high = n - 1

        while low <= high:
            mid = (low + high) // 2
            if matrix[i][mid] == target:
                return True
            elif matrix[i][mid] < target:
                low = mid + 1
            else:
                high = mid - 1
    return False


a = list(map(int, input().split()))
n1 = int(input())
print(searchMatrix(a, n1))

