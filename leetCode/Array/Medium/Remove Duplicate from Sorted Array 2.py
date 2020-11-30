def removeDuplicates(nums):
    tail = 0
    for num in nums:
        if tail < 2 or num > nums[tail - 2]:
            nums[tail] = num
            print(nums)
            tail += 1
    return tail


def removeDuplicates2(nums):
    tail = 0

    for num in nums:
        if tail < 2 or num > nums[tail - 2]:
            nums[tail] = num
            print(nums)
            tail += 1
            print(tail)
    return tail


a = list(map(int, input().split()))
print(removeDuplicates2(a))
