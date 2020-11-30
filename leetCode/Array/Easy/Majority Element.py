# solution 1:
def majorityElement(nums):
    for i in set(nums):
        if nums.count(i) > int(len(nums) / 2):
            return i


# solution 2:
def majorityElement2(nums):
    return sorted(nums)[int(len(nums) / 2)]


# solution 3:
# two pass + dictionary
def majorityElement3(nums):
    dic = {}
    for num in nums:
        dic[num] = dic.get(num, 0) + 1
        print(dic)
    for num in nums:
        if dic[num] > len(nums) // 2:
            return num


# solution 4:
# one pass + dictionary
def majorityElement4(nums):
    dic = {}
    j = 1
    for num in nums:
        print(f'iteration {j}')
        if num not in dic:
            print(f'if')
            dic[num] = 1
            print(dic)
        if dic[num] > len(nums) // 2:
            print('2nd if')
            return num
        else:
            print(f'else')
            dic[num] += 1
        j += 1
        print(dic)


# solution 5 (without any ds and module):
def majorityElement5(nums):
    count, candy = 0, 0

    i = 1
    for num in nums:
        print(f'iteration{i}')
        if num == candy:
            count += 1
            print(f'if')
            print(f'count {count}')
        elif count == 0:
            candy, count = num, 1
            print(f'elif')
            print(f'candy {candy} count {count}')
        else:
            count -= 1
            print('else')
            print(count)
        i += 1
        print()
    return candy


a = list(map(int, input().split()))
print(majorityElement5(a))

