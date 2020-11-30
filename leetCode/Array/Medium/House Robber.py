# dynamic programming:

def robber(nums):
    # Base Case: nums[0] = nums[0] >- len(nums) = 1
    # nums[1] = max(nums[1], nums[0]) >- len(nums) = 2
    # nums[k] = max(k + nums[k - 2], nums[k - 1]) > len(nums) = k

    # Approach 1:- Construct dp table
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]

    dp = [0] * len(nums)
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])
    print(dp)
    print()

    for i in range(2, len(nums)):
        dp[i] = max(nums[i] + dp[i - 2], dp[i - 1])
        print(dp)

    return dp[-1]


# Recursive relation:
def robber2(nums):
    def helper(index):
        print(index)

        # if we are at the end
        if index >= len(nums):
            print('if')
            return 0
        return max(helper(index + 1), nums[index] + helper(index + 2))
    print('after def')
    return helper(0)


# memoization:
def robber3(nums):
    memo = {}

    def helper(index):

        if index in memo:
            return memo[index]
        if index >= len(nums):
            return 0

        print(index)
        memo[index] = max(helper(index + 1), helper(index + 2) + nums[index])
        print(memo)
        return memo[index]

    return helper(0)


array = list(map(int, input().split()))
print(robber3(array))

