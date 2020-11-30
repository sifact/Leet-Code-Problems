# math solution:
def missingNumber(nums):
    n = len(nums)
    return int((n * (n + 1) / 2)) - sum(nums)


# a = list(map(int, input().split()))
# print(missingNumber(a))


