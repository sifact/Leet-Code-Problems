# Naive way:
def maximumProduct(nums):
    max_m = float('-inf')

    for i in range(len(nums)):
        for j in range(len(nums)):
            for k in range(len(nums)):
                if i != j and j != k and k != i:
                    product = nums[i] * nums[j] * nums[k]
                    max_m = max(max_m, product)
    return max_m


# Using sort():
def maximumProduct2(nums):
    return max(nums[0] * nums[1] * nums[-1], nums[-3], nums[-2], nums[-1])


a = list(map(int, input().split()))
print(maximumProduct(a))


