def sortColors(nums):
    for i in range(len(nums) - 1):
        if nums[i] > nums[i + 1]:
            nums[i], nums[i + 1] = nums[i + 1], nums[i]
    return nums


array = list(map(int, input().split()))
print(sortColors(array))
