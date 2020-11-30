def searchMatrix(matrix, target):
    if matrix:
        row, col, width = len(matrix) - 1, 0, len(matrix[0])

        while row >= 0 and col < width:
            print(matrix[row][col])
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                row = row - 1
            else:
                col = col + 1
    return False


m = []
for _ in range(int(input())):
    m.append(list(map(int, input().split())))

n1 = int(input())
print(searchMatrix(m, n1))

