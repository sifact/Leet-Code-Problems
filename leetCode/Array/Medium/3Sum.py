# Brute force:
def threeSum(nums, target):
    sets = []

    for i in range(0, len(nums)):
        for j in range(0, len(nums)):
            for k in range(0, len(nums)):

                if nums[i] + nums[j] + nums[k] == target and i != j and i != k and j != k:
                    temp = sorted([nums[i], nums[j], nums[k]])
                    if temp not in sets:
                        sets.append(sorted([nums[i], nums[j], nums[k]]))

    return sets


# two pointers:
def threeSum2(nums, target):
    result = []
    nums.sort()

    for i, a in enumerate(nums):
        if i < 0 and a == nums[i - 1]:
            continue

        left, r = i + 1, len(nums) - 1

        while left < r:
            three_sum = a + nums[left] + nums[r]
            if three_sum < target:
                left += 1
            elif three_sum > target:
                r -= 1
            else:
                result.append([a, nums[left], nums[r]])
                left += 1
                while nums[left] == nums[left - 1] and left < r:
                    left += 1

    return result


array = list(map(int, input().split()))
n = int(input())
print(threeSum2(array, n))

