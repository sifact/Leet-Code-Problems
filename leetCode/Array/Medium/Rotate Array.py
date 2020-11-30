def rotateArray(nums, k):
    k = k % len(nums)

    nums[:] = nums[-k:] + nums[:-k]
    return nums


a = list(map(int, input().split()))
n = int(input())
print(rotateArray(a, n))

