import itertools


def combinationSum2(nums, target):
    ret = []
    for i in range(target):
        for comb in itertools.combinations(nums, i + 1):
            if sum(comb) == target:

                if sorted(comb) not in ret:
                    ret.append(sorted(comb))
    return ret


a = list(map(int, input().split()))
n = int(input())
print(combinationSum2(a, n))


