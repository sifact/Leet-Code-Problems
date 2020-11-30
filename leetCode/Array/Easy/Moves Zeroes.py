# runtime 32 ms, memory usage 14.6
def moveZeroes(nums):
    zero = 0  # records the position of "0"
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[i], nums[zero] = nums[zero], nums[i]
            print(nums)
            zero += 1

    print()
    return nums


# runtime 152 ms memory usage 14.2:
def moveZeroes2(nums):
    for i in nums:
        print(i)
        nums.remove(0)
        nums.append(0)
        print(nums)

    # return nums


# two pointers:
def moveZeroes3(nums):
    slow = fast = 0
    while fast < len(nums):
        if nums[fast] != 0:
            nums[slow], nums[fast] = nums[fast], nums[slow]
            print(nums)

        # wait while we find a non-zero element to
        # switch with you
        if nums[slow] != 0:
            slow += 1

        # keep going
        fast += 1
    return nums


a = list(map(int, input().split()))
print(moveZeroes(a))
