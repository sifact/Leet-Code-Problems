# solution 1:
def mergeSortedArray(nums1, m, nums2, n):
    nums1[m:] = nums2[:]
    return nums1.sort()


num1 = list(map(int, input().split()))
n1 = int(input())
num2 = list(map(int, input().split()))
n2 = int(input())

print(mergeSortedArray(num1, n1, num2, n2))

# solution 2 (without sort()):


def merge(nums1, m, nums2, n):
    while m > 0 and n > 0:
        if nums1[m - 1] >= nums2[n - 1]:
            nums1[m + n - 1] = nums1[m - 1]
            m -= 1
        else:
            nums1[m + n - 1] = nums2[n - 1]
            n -= 1
    if n > 0:
        nums1[:n] = nums2[:n]



