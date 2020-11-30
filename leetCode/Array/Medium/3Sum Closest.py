def threeSumClosest(nums, target):
    ln = len(nums)
    result = nums[0] + nums[1] + nums[ln - 1]

    nums.sort()
    j = 0
    for i in range(ln):
        j += 1
        left, right = i + 1, ln - 1

        while left < right:
            cur_sum = nums[i] + nums[left] + nums[right]

            if cur_sum < target:
                left += 1
            else:
                right -= 1

            if abs(cur_sum - target) < abs(result - target):
                result = cur_sum
    return result


def threeSumCloser2(nums, target):
    nums.sort()
    res = sum(nums[:3])
    for i in range(len(nums)):
        left, r = i + 1, len(nums) - 1
        while left < r:
            s = nums[i] + nums[left] + nums[r]

            if abs(s - target) < abs(res - target):  # let's say 5 - 3 = 2 < 5 - 2 = 3; 3 is closest to 5
                res = s

            if s < target:
                left += 1
            elif s > target:
                r -= 1
            else:
                return res


a = list(map(int, input().split()))
n = int(input())
print(threeSumCloser2(a, n))
