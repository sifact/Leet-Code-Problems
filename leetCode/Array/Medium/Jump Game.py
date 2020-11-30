# 95 % fast
def canJump(nums):
    # The logic of this problem is:
    # maximum value + index must be grater than index

    m = 0
    for i, n in enumerate(nums):

        print(f'{i} iteration')
        if i > m:
            print(i, m)
            return False

        m = max(m, i + n)
        print(m)

    return True


# one liner version:
# def canJump2(nums):
# return reduce(lambda m, (i, n): max(m, i + n) * (i <= m), enumerate(nums, 1), 1 ) > 0


def canJump3(nums):
    goal = len(nums) - 1
    j = 0

    for i in range(len(nums))[::-1]:
        print(f'iteration{j}')
        if i + nums[i] >= goal:
            goal = i
            print(goal)
        j += 1
    return not goal


a = list(map(int, input().split()))
print(canJump3(a))

