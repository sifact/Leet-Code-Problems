import string


def isPalindrome(s):
    punch = string.punctuation

    for c in punch:
        if c in s:
            s = s.replace(c, '')

    space = ' '
    while space in s.lower():
        s = s.replace(space, '')

    left, right = 0, len(s) - 1
    s_low = s.lower()
    while left < right:
        if s_low[left] != s_low[right]:
            return False
        else:
            left += 1
            right -= 1
    return True


n = ''
print(isPalindrome(n))
