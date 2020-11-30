def findMin(nums):

    left, right = 0, len(nums) - 1

    while left < right:
        mid = (left + right) // 2

        if nums[mid] > nums[right]:
            # [3, 4, 5, 6, 7, 8, 9, 1, 2]
            left = mid + 1

        else:
            # nums[mid] <= nums[right]
            # [8, 9, 1, 2, 3, 4, 5, 6, 7]
            right = mid

    return nums[left]
