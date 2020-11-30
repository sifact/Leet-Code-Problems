# solution 1:


def removeElement(nums, val):
    while val in nums:
        nums.remove(val)
    return len(nums)


n = list(map(int, input().split()))
v = int(input())
print(removeElement(n, v))


# solution 2:
# Two pointers, one moving from left and one moving from the right
# When the left one finds an element equal to val, then it uses a non-val value from the right pointer

def removeElement2(nums, val):
    i = 0
    j = len(nums) - 1
    count_val = 0

    while i < len(nums):
        while j >= 0:
            if nums[j] != val:
                break
            j -= 1

        if nums[i] == val:
            nums[i] = nums[j]
            j -= 1
            count_val += 1

        i += 1
    return len(nums) - count_val

# solution 3:


def removeElement(nums, val):
    j = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[j] = nums[i]
            j += 1
    return j






