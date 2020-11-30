# two pointer:

def twoSum2(numbers, target):
    l, r = 0, len(numbers) - 1

    while l < r:
        s = numbers[l] + numbers[r]
        if s == target:
            return [l + 1, r + 1]
        elif s < target:
            l += 1
        else:
            r -= 1


# dictionary:
def twoSum02(numbers, target):
    dic = {}

    for idx, num in enumerate(numbers):
        diff = target - num
        if diff in dic:
            return dic[diff], num
        dic[num] = idx + 1


# brute-force-approach:
def twoSum03(nums, target):

    for i in range(len(nums) - 1):
        j = i + 1
        while j < len(nums):
            if nums[i] + nums[j] == target:

                return [i + 1, j + 1]
            j += 1


"""
    if not numbers or len(numbers) < 2:
        return [-1, -1]
    n = len(numbers)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if numbers[i] + numbers[j] == target:
                return [i + 1, j + 1]
    # return [-1, -1]
"""

a = list(map(int, input().split()))
m = int(input())
print(twoSum03(a, m))


