from itertools import combinations_with_replacement


# Backtracking/dfs:
def combinationSums(candidates, tar):
    def backTr(target, curr_sol, k):
        if target == 0:
            sol.append(curr_sol)

        if target < 0 or k >= len(candidates):
            return

        for i in range(k, len(candidates)):

            backTr(target - candidates[i], curr_sol + [candidates[i]], i)

    sol = []
    backTr(tar, [], 0)
    return sol


# Brute-force approach:
def combinationSum(nums, target):
    min_num = min(nums)
    ans = []
    for i in range(target // min_num):
        for comb in combinations_with_replacement(nums, i + 1):
            if sum(comb) == target:
                ans.append(comb)
    return ans


a = list(map(int, input().split()))
n = int(input())
print(combinationSum(a, n))
