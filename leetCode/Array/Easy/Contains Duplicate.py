# hash map solution:

def containDuplicate(nums):
    dup_map = {}

    for element in nums:
        if element in dup_map:
            return True
        else:
            dup_map[element] = 0
    return False


a = list(map(int, input().split()))
print(containDuplicate(a))


# solution 2:
def containDuplicate(nums):
    return len(nums) != len(set(nums))

