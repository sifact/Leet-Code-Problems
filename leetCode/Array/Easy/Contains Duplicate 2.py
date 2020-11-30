# Hash map-uh:
def containsDuplicate(nums, k):
    dup_map = {}

    for i, v in enumerate(nums):
        if v in dup_map and i - dup_map[v] <= k:
            return True
        dup_map[v] = i
    return False


# Using set:
def containDuplicate2(nums, k):
    seen = set()
    for i, num in enumerate(nums):
        if num in seen:
            return True
        seen.add(num)
        print(seen)
        if len(seen) > k:
            # if duplicate not in len(<=) k, that means it's not gonna True
            seen.remove(nums[i - k])
        print(seen)
    return False


a = list(map(int, input().split()))
n = int(input())
print(containDuplicate2(a, n))
