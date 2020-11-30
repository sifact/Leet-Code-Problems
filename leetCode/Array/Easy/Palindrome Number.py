# solution 1:
def isPalindrome(x):
    result = str(x)[::-1]
    return (x > 0) and result == str(x)


n = int(input())
print(isPalindrome(n))


# solution 2:
def isPalindrome(x):
    initial_x = x

    if x < 0:
        return False

    mirror = 0
    while x != 0:
        last_digit = x % 10
        mirror = mirror * 10 + last_digit
        x = x // 10

    return initial_x == mirror


x = int(input())
print(isPalindrome(x))


