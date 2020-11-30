# Bottom-up, 0(n) space:
def minimumTotal(triangle):
    if not triangle:
        return

    res = triangle[-1]
    print(res)
    for i in range(len(triangle) - 2, -1, -1):
        for j in range(len(triangle[i])):
            print(f'triangle {triangle[i][j]}')
            print(f'res j {res[j]}, {res[j + 1]}')
            print()
            res[j] = min(res[j], res[j + 1]) + triangle[i][j]
            print(res[j])
        print(res)

    return res[0]


array = []
for _ in range(int(input())):
    array.append(list(map(int, input().split())))

print(minimumTotal(array))
