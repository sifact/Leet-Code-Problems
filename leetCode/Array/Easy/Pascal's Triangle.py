def pascalsTriangle(numRows):
    res = [[] for _ in range(numRows)]

    for i in range(numRows):
        for j in range(i + 1):
            if j < i:
                if j == 0:
                    res[i].append(1)
                else:
                    res[i].append(res[i - 1][j - 1] + res[i - 1][j])
            if j == i:
                res[i].append(1)
    for i in range(len(res)):
        print(" " * (len(res) - 1 - i), res[i])


n = int(input())
pascalsTriangle(n)
