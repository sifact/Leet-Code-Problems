def balanceStringSplit(s):
    ans = 0
    balVar = 0

    for char in s:
        if char == 'R':
            balVar += -1
        if char == 'L':
            balVar += 1
        print(balVar)
        if balVar == 0:
            ans += 1

    return ans


n = input()
print(balanceStringSplit(n))

