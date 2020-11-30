# binary search
def search(nums, target):
    l, r = 0, len(nums) - 1

    while l <= r:
        mid = (l + r) // 2
        if target == nums[mid]:
            return mid

        # nums[left to mid] is sorted
        if nums[l] <= nums[mid]:
            if target > nums[mid] or target < nums[l]:
                l = mid + 1
            else:
                r = mid - 1
        # nums[mid to right] is sorted
        else:
            if target < nums[mid] or target > nums[r]:
                r = mid - 1
            else:
                l = mid + 1
    return -1


# binary search 2
def searchInRotatedSortedArray2(nums, target):
    i = 0
    while i < len(nums) - 1 and nums[i] <= nums[i + 1]:
        i += 1

    f_l, f_r = 0, i
    while f_l <= f_r:
        mid = (f_l + f_r) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            f_l += 1
        else:
            f_r -= 1

    s_l, s_r = i + 1, len(nums) - 1

    while s_l <= s_r:
        mid = (s_l + s_r) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            s_l += 1
        else:
            s_r -= 1

    return -1


a = list(map(int, input().split()))
n = int(input())
print(searchInRotatedSortedArray2(a, n))
