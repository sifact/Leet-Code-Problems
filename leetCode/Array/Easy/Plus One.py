# solution 1:
"""
We're given a list of digits, and the idea is to convert that list
to an integer, num. So each digit is multiplied by the proper
place value and added to num. For example, if digits = [2, 8, 2, 5]
then on the first iteration 3 is multiplied by 10 to the power 0f 4 - 1 - 0 = 3,
so this result in 3000, which is added to num. Then 8 is multiplied by 10 ** 2
and added to num, and so on.
"""


def plusOne(digits):
    num = 0
    for i in range(len(digits)):
        num += digits[i] * pow(10, (len(digits) - 1 - i))

    return [int(i) for i in str(num + 1)]


# solution 2:
def plusOne2(digits):
    carry0ver = 0
    for i in reversed(range(len(digits))):
        if digits[i] != 9:
            digits[i] += 1
            return digits
        else:
            digits[i] = 0
            if i == 0:
                digits.insert(0, 1)
    return digits


n = list(map(int, input().split()))
print(plusOne2(n))


