
# solution 1 (cheat):
def reverse(x):
    if x < 0:
        result = -int(str(-x)[::-1])
        return 0 if result < - 2 ** 31 else result
    else:
        result = int(str(x)[::-1])
        return 0 if result > 2 ** 31 - 1 else result


# solution 2:
def reverse2(x):
    positive = True
    maximum = pow(2, 31) - 1
    minimum = pow(-2, 31)

    if x < 0:
        positive = False
        x = x * -1
    x = int(str(x)[::-1])

    if not positive:
        x = x * -1

    if x > maximum or x < minimum:
        return 0
    else:
        return x

# solution 3:


def reverse3(x):
    out = 0
    isNeg = False
    if x < 0:
        isNeg = True
        x = -1 * x

    while x != 0:  # until quetiount == 0
        out = 10 * out + x % 10
        x = x // 10

    if out >= 2 ** 31 - 1 or -1 * out < -2 ** 31:
        return 0
    return out if not isNeg else -1 * out


n = int(input())
print(reverse(n))




