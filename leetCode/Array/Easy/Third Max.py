# Such a weird thinking )-:
def thirdMax(nums):
    nums_s = set(nums)
    n = 2
    while n and nums_s:
        nums_s.remove(max(nums_s))
        n -= 1
        if nums_s and n == 0:
            return max(nums_s)

    return max(nums)


# solution 2:
def thirdMax2(nums):
    if len(set(nums)) < 3:
        return max(nums)
    return sorted(set(nums))[-3]


a = list(map(int, input().split()))
print(thirdMax(a))
