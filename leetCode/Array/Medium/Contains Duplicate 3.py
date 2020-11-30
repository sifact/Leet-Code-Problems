def containsNearbyAlmostDuplicate(nums, k, t):

    for i in range(len(nums)):
        j = i + 1
        while j < len(nums):
            if abs(nums[i] - nums[j]) <= t and abs(i - j) <= k:
                return True
            j += 1
    return False


a = list(map(int, input().split()))
K, T = int(input()), int(input())
print(containsNearbyAlmostDuplicate(a, K, T))
