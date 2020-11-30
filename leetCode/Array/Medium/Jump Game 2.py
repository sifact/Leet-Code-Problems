def jumpGame2(nums, start):
    for i in range(len(nums)):
        if nums[start] == 0:
            return True
        start = start - nums[start]

    return False


a = list(map(int, input().split()))
n = int(input())
print(jumpGame2(a, n))
