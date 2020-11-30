
def maxSubArray(nums):
    maxSub, curSum = nums[0], 0

    for i in nums:

        if curSum < 0:
            curSum = 0
        curSum += i
        print(curSum)
        maxSub = max(maxSub, curSum)
    return maxSub


# solution 2 (kadane's algorithm)
def maxSubArray2(nums):
    max_current = max_global = nums[0]

    for num in range(1, len(nums)):
        max_current = max(max_current + nums[num], nums[num])

        max_global = max(max_global, max_current)
    return max_global


# dynamic programming
def maxSubArray3(nums):
    dp = [0] * len(nums)
    dp[0] = nums[0]

    # dp[1] = max(dp[0] + nums[1], nums[1])
    # dp[2] = max(dp[1] + nums[2], nums[2])

    for i in range(1, len(nums)):
        dp[i] = max(dp[i - 1] + nums[i], nums[i])

    return max(dp)


n = list(map(int, input().split()))
print(maxSubArray2(n))
