# Bubble sort
def bubbleSort(nums):
    k = 0
    p = 0
    for i in range(len(nums)):
        k += 1
        for j in range(len(nums) - i - 1):
            p += 1

            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    print(k)
    print(p)
    return nums


# Selection sort:
def selectionSort(nums):

    for i in range(len(nums)):
        index_min = i
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[index_min]:
                index_min = j

        if i != index_min:
            nums[i], nums[index_min] = nums[index_min], nums[i]

    return nums


# Insertion sort:
def insertionSort(nums):

    for i in range(1, len(nums)):
        item = nums[i]

        j = i - 1
        while j >= 0 and item < nums[j]:
            print('inside of while')
            nums[j + 1] = nums[j]

            j -= 1
        nums[j + 1] = item
    return nums


# array = list(map(int, input().split()))
# print(insertionSort(array))


# Merge sort:
def mergeSort(nums, left, right):

    if left >= right:
        return

    mid = (left + right) // 2
    # print(mid)

    mergeSort(nums, left, mid)

    mergeSort(nums, mid + 1, right)
    merge(nums, left, mid, right)


def merge(nums, left, mid, right):
    l_array = [0] * (mid - left + 1)
    r_array = [0] * (right - mid)



array = list(map(int, input().split()))
print(mergeSort(array, 0, len(array) - 1))

# 1 4 5 6 7 4 3 4
