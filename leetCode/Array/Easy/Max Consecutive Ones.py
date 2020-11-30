def maxConsecutiveOnes(nums):

    max_m, max_so_far = 0, 0
    for i in nums:
        if i == 0:
            max_so_far = 0
        else:
            max_so_far += 1
        max_m = max(max_m, max_so_far)
    return max_m


a = list(map(int, input().split()))
print(maxConsecutiveOnes(a))
