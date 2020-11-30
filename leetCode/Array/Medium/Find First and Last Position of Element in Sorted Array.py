# Naive way:
def searchRange2(nums, target):
    if target in nums:
        return [nums.index(target), nums.index(target) + nums.count(target) - 1]


# Binary search:
def searchRange(nums, target):
    left, r = 0, len(nums) - 1
    first, last = -1, -1

    while left <= r:
        mid = (left + r) // 2
        if nums[mid] <= target:
            if nums[mid] == target:
                last = mid
            left = mid + 1
        else:
            r = mid - 1

    left, r = 0, len(nums) - 1
    while left <= r:
        mid = (left + r) // 2
        if nums[mid] >= target:
            if nums[mid] == target:
                first = mid
            r = mid - 1
        else:
            left = mid + 1
    return [first, last]


a = list(map(int, input().split()))
n = int(input())
print(searchRange(a, n))
