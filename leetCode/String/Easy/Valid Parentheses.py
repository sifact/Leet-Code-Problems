def isValid(s):
    stack = []

    dic = {"]": '[', '}': '{', ')': '('}
    for char in s:
        if char in dic.values():
            print('if')
            stack.append(char)
            print(f'stack {stack}')
            print()

        elif char in dic.keys():
            print('elif')
            print(f'dic {dic[char]}')
            if stack == [] or dic[char] != stack.pop():
                return False

        else:
            print('else')
            return False

    return stack == []  # because of pop()


string = input()
print(isValid(string))
