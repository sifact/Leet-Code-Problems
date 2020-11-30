# inplace algorithm
def removeDuplicates(nums):
    idx = 1
    for i in range(1, len(nums) - 1):
        if nums[i - 1] != nums[i]:
            j = 0
            nums[idx] = nums[i]
            print(nums)
            idx += 1
    return idx


arr = list(map(int, input().split()))
print(removeDuplicates(arr))
