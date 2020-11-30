# Binary search:
def searchInsert(nums, target):
    low = 0
    high = len(nums) - 1

    while low <= high:
        mid = (low + high) // 2
        print(mid)
        print()
        if nums[mid] == target:
            print('if')
            return mid
        elif nums[mid] < target:
            print('elif')
            low = mid + 1
        else:
            print('else')
            high = mid - 1
            print(high)
    return low


# solution 2:

def searchInsert2(nums, target):

    if target in nums:
        return nums.index(target)

    nums.append(target)
    nums.sort()
    return nums.index(target)

# solution 3:


def searchInsert3(nums, target):
    return len([x for x in nums if x < target])


arr = list(map(int, input().split()))
n = int(input())
print(searchInsert(arr, n))

