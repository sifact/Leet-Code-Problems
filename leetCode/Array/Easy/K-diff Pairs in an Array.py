from collections import Counter


def findPairs(nums, k):
    # Count the elements with Counter
    # if k > 0 for each element i, check if i + k exist
    # if k == 0 for each element i, check if count[i] > 1

    hash_map = Counter(nums)
    count = 0
    for key in hash_map:
        if k > 1 and key + k in hash_map or k == 0 and hash_map[key] > 1:
            count += 1
    return count


# Generator expression
def findPairs2(nums, k):
    hash_map = Counter(nums)
    return sum(k > 0 and key + k in hash_map or k == 0 and hash_map[key] > 1 for key in hash_map)


a = list(map(int, input().split()))
num = int(input())
print(findPairs2(a, num))
