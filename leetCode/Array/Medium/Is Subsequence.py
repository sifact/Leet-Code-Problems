# O(n) recursion deletion edit distance
def isSubsequence(s, t):
    m = len(s)
    n = len(t)
    if n == 0:
        return True
    if m == 0:
        return False

    # base condition for first chars in s and t
    if m == 1:
        if n == 1:
            return (s[0] == t[0])
        else:
            return False

    # if last chars of s and t match - recursive call on deleting both chars
    if s[m - 1] == t[n - 1]:
        # print (s,t,m,n)
        return isSubsequence(t[:n - 1], s[:m - 1])
    else:
        # recursive call on only deleting source last char
        return isSubsequence(t[:n], s[:m - 1])

source, target = input(), input()
print(isSubsequence(source, target))

