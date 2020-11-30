def merge(nums):

    i = 0
    while i < len(nums) - 1:
        if nums[i][1] >= nums[i + 1][0]:
            nums[i][1] = max(nums[i][1], nums[i + 1][1])
            nums.remove(nums[i + 1])
        i += 1

    return nums


a = []
for _ in range(int(input())):
    a.append(list(map(int, input().split())))

print(merge(a))


