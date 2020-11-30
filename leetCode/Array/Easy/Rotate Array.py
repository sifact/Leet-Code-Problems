# time limit exceeded:
def rotateArray(nums, k):
    for i in range(k):
        tmp = nums[-1]
        nums[1:] = nums[:-1]
        nums[0] = tmp
    return nums


# solution 2:
def rotateArray2(nums, k):
    k = k % len(nums)
    return nums[-k:] + nums[:-k]


# solution 3:
def rotateArray3(nums, k):

    k = k % len(nums)
    nums[k:], nums[:k] = nums[:-k], nums[-k:]


arr = list(map(int, input().split()))
n = int(input())
print(rotateArray2(arr, n))



