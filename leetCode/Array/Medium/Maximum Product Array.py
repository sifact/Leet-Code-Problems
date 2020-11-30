def maxProduct(nums):
    mini, maxi, res = 1, 1, float('-inf')

    for n in nums:
        a = mini * n
        print(f'a {a}')
        b = maxi * n
        print(f'b {b}')

        print()
        mini = min(a, b, n)
        print(f'mini {mini}')
        maxi = max(a, b, n)
        print(f'maxi {maxi}')

        print()
        res = max(res, maxi)
        print(f'result {res}')

    return res


array = list(map(int, input().split()))
print(maxProduct(array))
