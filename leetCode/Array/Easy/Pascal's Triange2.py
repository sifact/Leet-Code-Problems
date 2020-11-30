# solution 1:

def getRow(rowIndex):
    row = [1] * (rowIndex + 1)

    for row_idx in range(2, rowIndex + 1):
        print('loop execute')
        for col_idx in range(row_idx - 1, 0, -1):
            row[col_idx] += row[col_idx - 1]

    return row

# solution 2:


def getRow2(rowIndex):
    row = [1]
    for _ in range(rowIndex):
        row = [x + y for x, y in zip([0] + row, row + [0])]
        print(row)

    return row


n = int(input())
print(getRow2(n))
