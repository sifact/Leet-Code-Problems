def findUnsortedSubArray(nums):

    def find_min_max(l, r):
        local_minimum = float('inf')
        local_maximum = float('-inf')

        for i in range(l, r + 1):
            if i == len(nums):
                break
            local_minimum = min(local_minimum, nums[i])
            local_maximum = max(local_maximum, nums[i])

        return local_minimum, local_maximum

    if len(nums) < 2:
        return 0

    l, r = 0, len(nums) - 1

    while l < r and nums[l] <= nums[l + 1]:
        l += 1

    while r > 0 and nums[r] >= nums[r - 1]:
        r -= 1

    if l > r:
        return 0

    tempMin, tempMax = find_min_max(l, r + 1)

    while l > 0 and tempMin < nums[l - 1]:
        l -= 1

    while r < len(nums) - 1 and tempMax > nums[r + 1]:
        r += 1

    return r - l + 1


def findUnsortedSubArray2(nums):
    is_same = [a == b for a, b in zip(nums, sorted(nums))]

    return 0 if all(is_same) else len(nums) - is_same.index(False) \
        - is_same[::-1].index(False)


def findUnsortedSubArray3(nums):
    sorted_nums = sorted(nums)
    if sorted_nums == nums:
        return 0

    start = 0
    while sorted_nums[start] == nums[start]:
        start += 1

    end = len(nums) - 1
    while sorted_nums[end] == nums[end]:
        end -= 1

    return end + 1 - start


a = list(map(int, input().split()))
print(findUnsortedSubArray3(a))


















