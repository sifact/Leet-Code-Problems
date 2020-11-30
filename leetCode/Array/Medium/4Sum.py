# Brute force:
def fourSum(nums, target):
    sets = []

    for i in range(0, len(nums)):
        for j in range(0, len(nums)):
            for k in range(0, len(nums)):
                for L in range(0, len(nums)):

                    if nums[i] + nums[j] + nums[k] + nums[L] == target and i != j and i != k and j != k \
                            and i != L and L != j and L != k:
                        temp = sorted([nums[i], nums[j], nums[k], nums[L]])
                        if temp not in sets:
                            sets.append(sorted([nums[i], nums[j], nums[k], nums[L]]))

    return sets


# Hash map-uh:
def fourSum2(nums, target):
    d = dict()
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            sum2 = nums[i] + nums[j]
            if sum2 in d:
                d[sum2].append((i, j))
            else:
                d[sum2] = [(i, j)]
    print(d)

    result = set()
    for key in d:
        value = target - key
        print(value)
        if value in d:
            list1 = d[key]
            print(list1)
            list2 = d[value]
            print(list2)
            for i, j in list1:
                for k, l in list2:
                    if i != k and i != l and j != k and j != l:
                        f_list = [nums[i], nums[j], nums[k], nums[l]]
                        f_list.sort()
                        result.add(tuple(f_list))

    return list(result)


# two pointers
def fourSum3(self, nums, target):

    def findNsum(left, r, target, N, result, results):
        if r - left + 1 < N or N < 2 or target < nums[left] * N or target > nums[r] * N:  # early termination
            return
        if N == 2:  # two pointers solve sorted 2-sum problem
            while left < r:
                s = nums[left] + nums[r]
                if s == target:
                    results.append(result + [nums[left], nums[r]])
                    left += 1
                    while left < r and nums[left] == nums[left - 1]:
                        left += 1
                elif s < target:
                    left += 1
                else:
                    r -= 1
        else:  # recursively reduce N
            for i in range(left, r + 1):
                if i == left or (i > left and nums[i - 1] != nums[i]):
                    findNsum(i + 1, r, target - nums[i], N - 1, result + [nums[i]], results)

    nums.sort()
    results = []
    findNsum(0, len(nums) - 1, target, 4, [], results)
    return results


a = list(map(int, input().split()))
n = int(input())
print(fourSum2(a, n))
