def rotate(nums, target):
    l, r = 0, len(nums)-1
    while l <= r:
        mid = l + (r-l)//2
        if nums[mid] == target:
            return True
        while l < mid and nums[l] == nums[mid]: # tricky part
            l += 1
        # the first half is ordered
        if nums[l] <= nums[mid]:
            # target is in the first half
            if nums[l] <= target < nums[mid]:
                r = mid - 1
            else:
                l = mid + 1
        # the second half is ordered
        else:
            # target is in the second half
            if nums[mid] < target <= nums[r]:
                l = mid + 1
            else:
                r = mid - 1
    return False


def rotate2(nums, target):
    if not len(nums):
        return False
    i = 0
    while i < len(nums) - 1 and nums[i] <= nums[i + 1]:
        i += 1

    f_l, f_r = 0, i

    while f_l <= f_r:
        mid = (f_l + f_r) // 2
        if nums[mid] == target:
            return True
        elif nums[mid] < target:
            f_l = mid + 1
        else:
            f_r = mid - 1

    l_l, l_r = i + 1, len(nums) - 1

    while l_l <= l_r:
        mid = (l_l + l_r) // 2
        if nums[mid] == target:
            return True
        elif nums[mid] < target:
            l_l = mid + 1
        else:
            l_r = mid - 1
    return False
