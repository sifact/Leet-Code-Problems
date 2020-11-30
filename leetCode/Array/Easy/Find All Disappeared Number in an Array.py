def findDisappearedNumbers(nums):
    # for each number i in nums,
    # we mark the number that i points in negative
    # then we filter the list, get all the indexes
    # who points to a positive number

    for i in range(len(nums)):
        index = abs(nums[i]) - 1

        nums[index] = -abs(nums[index])
    return [i + 1 for i in range(len(nums)) if nums[i] > 0]


# Using Hash table:
def findDisappearedNumbers2(nums):
    hash_table = {}
    for num in nums:
        hash_table[num] = 1

    empty_list = []
    for i in range(1, len(nums) + 1):
        if i not in hash_table:
            empty_list.append(i)

    return empty_list


# Using set:
def findDisappearedNumbers3(nums):
    returned_array = []

    set_array = set(nums)
    for i in range(1, len(nums) + 1):
        if i not in set_array:
            returned_array.append(i)

    return returned_array


a = list(map(int, input().split()))
print(findDisappearedNumbers3(a))
