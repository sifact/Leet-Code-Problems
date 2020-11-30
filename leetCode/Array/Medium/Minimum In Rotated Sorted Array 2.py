def findMin(nums):
    left, right = 0, len(nums)

    while left < right:
        mid = (left + right) // 2

        if nums[mid] > nums[right]:
            left = mid + 1

        elif nums[mid] < nums[left]:
            right = mid
            left += 1

        else:
            right -= 1

    return nums[left]