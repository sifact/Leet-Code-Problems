from itertools import combinations


def subsets(nums):
    res = []

    for i in range(len(nums) + 1):
        for comb in combinations(nums, i):
            res.append(comb)

    return res


# solution 2:
def subSets(nums):
    res = [[]]
    for num in nums:
        res += [i + [num] for i in res]
        print(res)
    return res


# solution 3 (recursive solution):
def subSets2(nums):
    ret = []
    dfs(nums, [], ret)
    return ret


def dfs(nums, path, ret):
    ret.append(path)
    print(f'result {ret}')
    print(f'nums {nums}')

    for i in range(len(nums)):
        print(f'i {i}')
        print(f'path {path}')
        print(f'nums {nums[i]}')
        print()
        dfs(nums[i + 1:], path + [nums[i]], ret)
        print('Back')


a = list(map(int, input().split()))
print(subSets2(a))
