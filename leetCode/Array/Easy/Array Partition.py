def arrayPairSum(nums):
    nums.sort()
    total = 0
    for i in range(0, len(nums), 2):
        total += nums[i]
    return total


def arrayPairSum2(nums):
    return sum(sorted(nums)[::2])


a = list(map(int, input().split()))
print(arrayPairSum2(a))

