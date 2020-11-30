def twoSum(arr, target):
    prevMap = {}  # val : index

    for i, n in enumerate(arr):
        diff = target - n
        if diff in prevMap:
            return [prevMap[diff], i]
        prevMap[n] = i


a = list(map(int, input().split()))
num = int(input())
print(twoSum(a, num))

# time complexity 0(n) space complexity 0(n)










